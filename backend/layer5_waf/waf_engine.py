SQLI_PATTERNS = [
    "' OR 1=1",
    "UNION SELECT",
    "DROP TABLE",
    "--",
]

XSS_PATTERNS = [
    "<script>",
    "javascript:",
    "onerror=",
    "onload="
]

def waf_check(payload):

    if not payload:
        return True, "clean"

    text = payload.lower()

    for attack in SQLI_PATTERNS:
        if attack.lower() in text:
            return False, "SQL Injection"

    for attack in XSS_PATTERNS:
        if attack.lower() in text:
            return False, "XSS Attack"

    return True, "clean"