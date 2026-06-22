allowed_protocols = [
    "HTTP",
    "HTTPS",
    "SSH",
    "DNS"
]

def validate_protocol(protocol):
    return protocol.upper() in allowed_protocols