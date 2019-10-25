# Copyright: 2019, NLnet Labs and the Internet.nl contributors
# SPDX-License-Identifier: Apache-2.0

# --- STATUSES
#
# Do not change these values.
# You can append statuses and then change the ORDERED_STATUSES below.
STATUS_FAIL = 0
STATUS_SUCCESS = 1
STATUS_NOTICE = 2
STATUS_GOOD_NOT_TESTED = 3
STATUS_NOT_TESTED = 4
STATUS_INFO = 5

STATUS_MAX = STATUS_SUCCESS

# The highest status MUST be the one defined in STATUS_MAX above.
ORDERED_STATUSES = {
    STATUS_FAIL: 0,
    STATUS_NOTICE: 1,
    STATUS_INFO: 2,
    STATUS_GOOD_NOT_TESTED: 3,
    STATUS_NOT_TESTED: 4,
    STATUS_SUCCESS: 5
}


# --- SCORES
#
FULL_WEIGHT_POINTS = 10  # These are three levels of weighing results.
HALF_WEIGHT_POINTS = 5   # All three can be used for passed tests, the
LESS_WEIGHT_POINTS = 2   # difference is the effect on the overall score.
NO_POINTS = 0


# You can edit the below values to change the scoring for the subtests.
# The _WORST_STATUS reflects what is the worst result for that test when
# generating the results. Currently you can choose between:
#   - STATUS_FAIL (Mandatory test, will impact the overall score)
#   - STATUS_NOTICE (Optional test, will not affect the overall score)
#   - STATUS_INFO (Informational test, will not affect the overall score)


# --- SHARED
#
IPV6_NS_CONN_GOOD = FULL_WEIGHT_POINTS
IPV6_NS_CONN_PARTIAL = LESS_WEIGHT_POINTS
IPV6_NS_CONN_FAIL = NO_POINTS
IPV6_NS_CONN_WORST_STATUS = STATUS_FAIL


# --- WEBTEST
#
WEB_IPV6_WS_CONN_GOOD = FULL_WEIGHT_POINTS
WEB_IPV6_WS_CONN_PARTIAL = LESS_WEIGHT_POINTS
WEB_IPV6_WS_CONN_FAIL = NO_POINTS
WEB_IPV6_WS_CONN_WORST_STATUS = STATUS_FAIL

WEB_IPV6_WS_SIMHASH_OK = LESS_WEIGHT_POINTS
WEB_IPV6_WS_SIMHASH_FAIL = NO_POINTS
WEB_IPV6_WS_SIMHASH_WORST_STATUS = STATUS_FAIL

WEB_DNSSEC_SECURE = FULL_WEIGHT_POINTS
WEB_DNSSEC_INSECURE = LESS_WEIGHT_POINTS
WEB_DNSSEC_BOGUS = NO_POINTS
WEB_DNSSEC_ERROR = NO_POINTS
WEB_DNSSEC_WORST_STATUS = STATUS_FAIL

# The HTTPS_EXISTS test is not scored. The scoring of the category relies on
# the subsequent tests.
WEB_TLS_HTTPS_EXISTS_WORST_STATUS = STATUS_FAIL

WEB_TLS_FORCED_HTTPS_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_FORCED_HTTPS_NO_HTTP = FULL_WEIGHT_POINTS
WEB_TLS_FORCED_HTTPS_BAD = NO_POINTS
WEB_TLS_FORCED_HTTPS_WORST_STATUS = STATUS_FAIL

WEB_TLS_HTTP_COMPRESSION_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_HTTP_COMPRESSION_BAD = NO_POINTS
WEB_TLS_HTTP_COMPRESSION_WORST_STATUS = STATUS_INFO

WEB_TLS_HSTS_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_HSTS_PARTIAL = LESS_WEIGHT_POINTS
WEB_TLS_HSTS_BAD = NO_POINTS
WEB_TLS_HSTS_WORST_STATUS = STATUS_FAIL

WEB_TLS_PROTOCOLS_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_PROTOCOLS_OK = HALF_WEIGHT_POINTS
WEB_TLS_PROTOCOLS_BAD = NO_POINTS
WEB_TLS_PROTOCOLS_WORST_STATUS = STATUS_FAIL

WEB_TLS_SUITES_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_SUITES_OK = FULL_WEIGHT_POINTS
WEB_TLS_SUITES_BAD = NO_POINTS
WEB_TLS_SUITES_WORST_STATUS = STATUS_FAIL

WEB_TLS_CIPHER_ORDER_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_CIPHER_ORDER_OK = FULL_WEIGHT_POINTS
WEB_TLS_CIPHER_ORDER_BAD = NO_POINTS
WEB_TLS_CIPHER_ORDER_WORST_STATUS = STATUS_FAIL

WEB_TLS_FS_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_FS_OK = FULL_WEIGHT_POINTS
WEB_TLS_FS_BAD = NO_POINTS
WEB_TLS_FS_WORST_STATUS = STATUS_FAIL

WEB_TLS_COMPRESSION_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_COMPRESSION_BAD = NO_POINTS
WEB_TLS_COMPRESSION_WORST_STATUS = STATUS_FAIL

WEB_TLS_SECURE_RENEG_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_SECURE_RENEG_BAD = NO_POINTS
WEB_TLS_SECURE_RENEG_WORST_STATUS = STATUS_FAIL

WEB_TLS_CLIENT_RENEG_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_CLIENT_RENEG_BAD = NO_POINTS
WEB_TLS_CLIENT_RENEG_WORST_STATUS = STATUS_FAIL

WEB_TLS_TRUSTED_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_TRUSTED_BAD = NO_POINTS
WEB_TLS_TRUSTED_WORST_STATUS = STATUS_FAIL

WEB_TLS_PUBKEY_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_PUBKEY_OK = FULL_WEIGHT_POINTS
WEB_TLS_PUBKEY_BAD = NO_POINTS
WEB_TLS_PUBKEY_WORST_STATUS = STATUS_FAIL

WEB_TLS_SIGNATURE_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_SIGNATURE_BAD = NO_POINTS
WEB_TLS_SIGNATURE_WORST_STATUS = STATUS_FAIL

WEB_TLS_HOSTMATCH_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_HOSTMATCH_BAD = NO_POINTS
WEB_TLS_HOSTMATCH_WORST_STATUS = STATUS_FAIL

# DANE_EXISTS has no score. It is combined with
# DANE_VALID below.
WEB_TLS_DANE_EXISTS_WORST_STATUS = STATUS_INFO

WEB_TLS_DANE_VALIDATED = FULL_WEIGHT_POINTS
WEB_TLS_DANE_NONE = NO_POINTS
WEB_TLS_DANE_NONE_BOGUS = NO_POINTS
WEB_TLS_DANE_FAILED = NO_POINTS
WEB_TLS_DANE_VALID_WORST_STATUS = STATUS_NOTICE

# DANE_ROLLOVER has no score.
WEB_TLS_DANE_ROLLOVER_WORST_STATUS = STATUS_NOTICE

WEB_TLS_ZERO_RTT_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_ZERO_RTT_BAD = NO_POINTS
WEB_TLS_ZERO_RTT_WORST_STATUS = STATUS_FAIL

WEB_TLS_OCSP_STAPLING_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_OCSP_STAPLING_OK = FULL_WEIGHT_POINTS
WEB_TLS_OCSP_STAPLING_BAD = NO_POINTS
WEB_TLS_OCSP_STAPLING_WORST_STATUS = STATUS_NOTICE

WEB_TLS_HASH_FUNC_GOOD = FULL_WEIGHT_POINTS
WEB_TLS_HASH_FUNC_OK = FULL_WEIGHT_POINTS
WEB_TLS_HASH_FUNC_BAD = NO_POINTS
WEB_TLS_HASH_FUNC_WORST_STATUS = STATUS_NOTICE

WEB_APPSECPRIV_X_FRAME_OPTIONS_GOOD = FULL_WEIGHT_POINTS
WEB_APPSECPRIV_X_FRAME_OPTIONS_BAD = NO_POINTS
WEB_APPSECPRIV_X_FRAME_OPTIONS_WORST_STATUS = STATUS_NOTICE

WEB_APPSECPRIV_X_CONTENT_TYPE_OPTIONS_GOOD = FULL_WEIGHT_POINTS
WEB_APPSECPRIV_X_CONTENT_TYPE_OPTIONS_BAD = NO_POINTS
WEB_APPSECPRIV_X_CONTENT_TYPE_OPTIONS_WORST_STATUS = STATUS_NOTICE

WEB_APPSECPRIV_X_XSS_PROTECTION_GOOD = FULL_WEIGHT_POINTS
WEB_APPSECPRIV_X_XSS_PROTECTION_BAD = NO_POINTS
WEB_APPSECPRIV_X_XSS_PROTECTION_WORST_STATUS = STATUS_NOTICE

WEB_APPSECPRIV_REFERRER_POLICY_GOOD = FULL_WEIGHT_POINTS
WEB_APPSECPRIV_REFERRER_POLICY_BAD = FULL_WEIGHT_POINTS
WEB_APPSECPRIV_REFERRER_POLICY_WORST_STATUS = STATUS_NOTICE

WEB_APPSECPRIV_CONTENT_SECURITY_POLICY_GOOD = FULL_WEIGHT_POINTS
WEB_APPSECPRIV_CONTENT_SECURITY_POLICY_BAD = NO_POINTS
WEB_APPSECPRIV_CONTENT_SECURITY_POLICY_WORST_STATUS = STATUS_INFO


# --- MAILTEST
#
MAIL_IPV6_MX_CONN_GOOD = FULL_WEIGHT_POINTS
MAIL_IPV6_MX_CONN_PARTIAL = LESS_WEIGHT_POINTS
MAIL_IPV6_MX_CONN_FAIL = NO_POINTS
MAIL_IPV6_MX_CONN_WORST_STATUS = STATUS_FAIL

MAIL_DNSSEC_SECURE = FULL_WEIGHT_POINTS
MAIL_DNSSEC_INSECURE = LESS_WEIGHT_POINTS
MAIL_DNSSEC_BOGUS = NO_POINTS
MAIL_DNSSEC_ERROR = NO_POINTS
MAIL_DNSSEC_WORST_STATUS = STATUS_FAIL

MAIL_AUTH_DKIM_PASS = FULL_WEIGHT_POINTS
MAIL_AUTH_DKIM_FAIL = NO_POINTS
MAIL_AUTH_DKIM_ERROR = NO_POINTS
MAIL_AUTH_DKIM_WORST_STATUS = STATUS_FAIL

MAIL_AUTH_DMARC_PASS = FULL_WEIGHT_POINTS
MAIL_AUTH_DMARC_FAIL = NO_POINTS
MAIL_AUTH_DMARC_ERROR = NO_POINTS
MAIL_AUTH_DMARC_WORST_STATUS = STATUS_FAIL

MAIL_AUTH_DMARC_POLICY_PASS = FULL_WEIGHT_POINTS
MAIL_AUTH_DMARC_POLICY_PARTIAL = LESS_WEIGHT_POINTS
MAIL_AUTH_DMARC_POLICY_FAIL = NO_POINTS
MAIL_AUTH_DMARC_POLICY_WORST_STATUS = STATUS_FAIL

MAIL_AUTH_SPF_PASS = FULL_WEIGHT_POINTS
MAIL_AUTH_SPF_FAIL = NO_POINTS
MAIL_AUTH_SPF_ERROR = NO_POINTS
MAIL_AUTH_SPF_WORST_STATUS = STATUS_FAIL

MAIL_AUTH_SPF_POLICY_PASS = FULL_WEIGHT_POINTS
MAIL_AUTH_SPF_POLICY_PARTIAL = LESS_WEIGHT_POINTS
MAIL_AUTH_SPF_POLICY_FAIL = NO_POINTS
MAIL_AUTH_SPF_POLICY_WORST_STATUS = STATUS_FAIL

# The STARTTLS_EXISTS test is not scored. The scoring of the category relies on
# the subsequent tests.
MAIL_TLS_STARTTLS_EXISTS_WORST_STATUS = STATUS_FAIL

MAIL_TLS_PROTOCOLS_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_PROTOCOLS_OK = FULL_WEIGHT_POINTS
MAIL_TLS_PROTOCOLS_BAD = NO_POINTS
MAIL_TLS_PROTOCOLS_WORST_STATUS = STATUS_FAIL

MAIL_TLS_SUITES_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_SUITES_OK = FULL_WEIGHT_POINTS
MAIL_TLS_SUITES_BAD = NO_POINTS
MAIL_TLS_SUITES_WORST_STATUS = STATUS_FAIL

MAIL_TLS_CIPHER_ORDER_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_CIPHER_ORDER_OK = FULL_WEIGHT_POINTS
MAIL_TLS_CIPHER_ORDER_BAD = NO_POINTS
MAIL_TLS_CIPHER_ORDER_WORST_STATUS = STATUS_FAIL

MAIL_TLS_FS_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_FS_OK = FULL_WEIGHT_POINTS
MAIL_TLS_FS_BAD = NO_POINTS
MAIL_TLS_FS_WORST_STATUS = STATUS_FAIL

MAIL_TLS_COMPRESSION_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_COMPRESSION_BAD = NO_POINTS
MAIL_TLS_COMPRESSION_WORST_STATUS = STATUS_FAIL

MAIL_TLS_SECURE_RENEG_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_SECURE_RENEG_BAD = NO_POINTS
MAIL_TLS_SECURE_RENEG_WORST_STATUS = STATUS_FAIL

MAIL_TLS_CLIENT_RENEG_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_CLIENT_RENEG_BAD = NO_POINTS
MAIL_TLS_CLIENT_RENEG_WORST_STATUS = STATUS_NOTICE

MAIL_TLS_TRUSTED_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_TRUSTED_BAD = NO_POINTS
MAIL_TLS_TRUSTED_WORST_STATUS = STATUS_INFO

MAIL_TLS_PUBKEY_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_PUBKEY_OK = FULL_WEIGHT_POINTS
MAIL_TLS_PUBKEY_BAD = NO_POINTS
MAIL_TLS_PUBKEY_WORST_STATUS = STATUS_FAIL

MAIL_TLS_SIGNATURE_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_SIGNATURE_BAD = NO_POINTS
MAIL_TLS_SIGNATURE_WORST_STATUS = STATUS_FAIL

MAIL_TLS_HOSTMATCH_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_HOSTMATCH_BAD = NO_POINTS
MAIL_TLS_HOSTMATCH_WORST_STATUS = STATUS_INFO

# DANE_EXISTS has no score. It is combined with
# DANE_VALID below.
MAIL_TLS_DANE_EXISTS_WORST_STATUS = STATUS_FAIL

MAIL_TLS_DANE_VALIDATED = FULL_WEIGHT_POINTS
MAIL_TLS_DANE_NONE = NO_POINTS
MAIL_TLS_DANE_NONE_BOGUS = NO_POINTS
MAIL_TLS_DANE_FAILED = NO_POINTS
MAIL_TLS_DANE_VALID_WORST_STATUS = STATUS_FAIL

# DANE_ROLLOVER has no score.
MAIL_TLS_DANE_ROLLOVER_WORST_STATUS = STATUS_INFO

MAIL_TLS_ZERO_RTT_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_ZERO_RTT_BAD = NO_POINTS
MAIL_TLS_ZERO_RTT_WORST_STATUS = STATUS_FAIL

MAIL_TLS_OCSP_STAPLING_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_OCSP_STAPLING_OK = FULL_WEIGHT_POINTS
MAIL_TLS_OCSP_STAPLING_BAD = NO_POINTS
MAIL_TLS_OCSP_STAPLING_WORST_STATUS = STATUS_NOTICE

MAIL_TLS_HASH_FUNC_GOOD = FULL_WEIGHT_POINTS
MAIL_TLS_HASH_FUNC_OK = FULL_WEIGHT_POINTS
MAIL_TLS_HASH_FUNC_BAD = NO_POINTS
MAIL_TLS_HASH_FUNC_WORST_STATUS = STATUS_NOTICE
