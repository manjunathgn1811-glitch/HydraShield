SUSPICIOUS_PATTERNS = [
    "<script>",
    "cmd.exe",
    "powershell",
    "DROP TABLE",
    "/etc/passwd",
    "../"
]

def inspect_payload(payload):
    if not payload:
        return True, "clean"

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern.lower() in payload.lower():
            return False, f"Detected: {pattern}"

    return True, "clean"