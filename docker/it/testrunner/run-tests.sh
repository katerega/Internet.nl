#!/bin/bash
# This script performs post deployment setup tasks on the root, master and resolver servers
# in the cluster created by docker-compose up.
# This script expects environment variable COMPOSE_PROJECT_NAME to be set. The intention is
# that it is passed in by the docker-compose.yml file, e.g.:
#   environment:
#     - COMPOSE_PROJECT_NAME
# and also used when invoking docker-compose, e.g.
#   COMPOSE_PROJECT_NAME=blah docker-compose up
# This will result in container names being prefixed by COMPOSE_PROJECT_NAME. Otherwise the
# default is 'it', as that is the directory the integration test docker-compose.yml file is
# in and thus that is the default project name used by Docker compose.

set -e -u

COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME:-it}

# assumes that scale=1 for the specified container
container_name() {
    CONTAINER_NAME="$1"
    echo "${COMPOSE_PROJECT_NAME}_${CONTAINER_NAME}_1"
}

wait_for_container_up() {
    CONTAINER_NAME="$1"
    SECONDS_TO_WAIT=${2:-15}

    UP=0
    while [ ${SECONDS_TO_WAIT} -ge 1 ]; do
        echo -n "Waiting ${SECONDS_TO_WAIT} seconds for Docker container ${CONTAINER_NAME} to be up: "
        STATE=$(docker inspect --format "{{.State.Running}}" ${CONTAINER_NAME} || true)
        echo ${STATE}
        [ "${STATE}" == "true" ] && UP=1 && break
        sleep 1s
        let "SECONDS_TO_WAIT=SECONDS_TO_WAIT-1"
    done

    if [ $UP -eq 1 ]; then
        echo "Docker container ${CONTAINER_NAME} is up"
        return 0
    else
        echo >&2 "Docker container ${CONTAINER_NAME} is still NOT Up"
        return 1
    fi
}

wait_for_port_connect() {
    FQDN="$1"
    PORT="$2"
    SECONDS_TO_WAIT=${3:-15}

    CONNECTED=0
    while [ ${SECONDS_TO_WAIT} -ge 1 ]; do
        echo "Waiting ${SECONDS_TO_WAIT} seconds to connect to ${FQDN}:${PORT}.."
        nc -z ${FQDN} ${PORT} && CONNECTED=1 && break
        sleep 1s
        let "SECONDS_TO_WAIT=SECONDS_TO_WAIT-1"
    done

    if [ $CONNECTED -eq 1 ]; then
        echo "Connected to ${FQDN}:${PORT}"
        return 0
    else
        echo >&2 "UNABLE to connect to ${FQDN}:${PORT}"
        return 1
    fi
}

sign_zone() {
    ZONE_DOMAIN="$1"
    ZONE_NSD_CONTAINER="$2"

    echo
    echo ":: Signing zone '${ZONE_DOMAIN}''.."
    wait_for_container_up ${ZONE_NSD_CONTAINER}

    SIGN_CMD="docker exec ${ZONE_NSD_CONTAINER} /opt/nsd-sign-zone.sh"

    if [ "${ZONE_DOMAIN}" == "." ]; then
        ${SIGN_CMD} . root
    else
        PARENT_NSD_CONTAINER="$3"
        PARENT_DOMAIN=$(echo ${ZONE_DOMAIN} | cut -d . -f 2-)
        ZONE_FILE=${ZONE_DOMAIN}
        PARENT_ZONE_FILE=${PARENT_DOMAIN}

        if [ "${PARENT_DOMAIN}" == "${ZONE_DOMAIN}" ]; then
            PARENT_DOMAIN=.
            PARENT_ZONE_FILE=root
        fi

        wait_for_container_up ${PARENT_NSD_CONTAINER}
        ${SIGN_CMD} \
            ${ZONE_DOMAIN} ${ZONE_FILE} \
            ${PARENT_DOMAIN} ${PARENT_ZONE_FILE} \
            ${PARENT_NSD_CONTAINER}
    fi
}

C_ROOT=$(container_name root)
C_MASTER=$(container_name master)
C_SUBMASTER=$(container_name submaster)
C_RESOLVER=$(container_name resolver)
C_APP=$(container_name app)

sign_zone test.nlnetlabs.nl $C_SUBMASTER $C_SUBMASTER
sign_zone nlnetlabs.nl $C_SUBMASTER $C_MASTER
sign_zone nl $C_MASTER $C_ROOT
sign_zone . $C_ROOT

echo
echo ':: Retrieving root trust anchor for use by the resolver..'
# Not sure why docker cp root:/tmp/zsk.key /tmp/root_zsk.key doesn't work...
docker exec $C_ROOT cat /tmp/zsk.key >/tmp/root_zsk.key

echo
echo ':: Installing root trust anchor in the resolver..'
wait_for_container_up $C_RESOLVER
docker cp /tmp/root_zsk.key $C_RESOLVER:/var/lib/unbound/my-root.key
docker exec $C_RESOLVER perl -pi -e 's|^#   auto-trust-anchor-file:.+|   auto-trust-anchor-file: "/var/lib/unbound/my-root.key"|' /etc/unbound/unbound.conf
docker exec $C_RESOLVER unbound-control reload

echo
echo ':: Verify DNS lookup from resolver -> master -> root with DNSSEC'
dig +dnssec @${RESOLVER_IP} tls1213.test.nlnetlabs.nl

echo
echo ':: Checking DNSSEC trust tree'
docker exec $C_RESOLVER drill @127.0.0.1 SOA IN -DSk /var/lib/unbound/my-root.key -r /etc/unbound/root.hints tls1213.test.nlnetlabs.nl

echo
echo ':: Installing root trust anchor in the app container..'
docker cp /tmp/root_zsk.key $C_APP:/tmp/root_zsk.key

PROTOCOLS="ssl2 ssl3 tls1 tls1_1 tls1_2 tls1_3"
TARGETS="nossl tls1213 tls1213sni tls1213wrongcertname tls1213nohsts tls10only tls11only tls12only tls13only ssl2only ssl3only"
SUFFIX=".test.nlnetlabs.nl"

echo
echo ':: Dumping target domain TLS cert to hostname mappings'
for N in ${TARGETS}; do
    echo -n -e "$N:\t"
    FQDN="${N}${SUFFIX}"
    openssl s_client -showcerts -verify_return_error -brief ${FQDN}:443 2>&1 | grep -Eo "CN = .+" || echo ERROR
done | column -t

echo
echo ':: Dumping target domain TLS version support'
for N in $TARGETS; do
    FQDN="${N}${SUFFIX}"
    echo -n "${N}: "
    for PROT in ${PROTOCOLS}; do
        echo -n "${PROT}: "
        SUPPORTED='-'
        echo GET / | openssl s_client -${PROT} -servername ${FQDN} -connect ${FQDN}:443 &>/dev/null && SUPPORTED='YES'
        echo -n -e "${SUPPORTED}\t"
    done
    echo
done | column -t

echo
echo ':: Waiting for Internet.nl app to become available..'
wait_for_container_up $C_APP
wait_for_port_connect app 8080 60

# TODO: sleeps are brittle, replace this with a deterministic check
echo
echo ':: Wait 15 seconds to give the app time to settle, e.g. Celery worker startup etc..'
sleep 15s

echo
echo ':: Execute the browser based integration test suite..'

PYTEST_PROGRESS_ARGS="--show-progress"
PYTEST_SELENIUM_ARGS="--driver Remote --host selenium --port 4444 --capability browserName firefox"
PYTEST_HTML_ARGS="--html=/tmp/it-report/$(date +'%Y%m%d_%H%M%S').html"

docker exec $C_APP sudo mkdir -p /tmp/it-report/coverage-data
docker exec $C_APP sudo chmod -R a+w /tmp/it-report
docker exec $C_APP pytest \
    ${PYTEST_PROGRESS_ARGS} \
    ${PYTEST_HTML_ARGS} \
    ${PYTEST_SELENIUM_ARGS} || true

docker exec $C_APP /opt/coverage-finalize.sh