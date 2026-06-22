malicious_ips = {
    "1.1.1.1",
    "8.8.8.8"
}

def reputation_check(ip):
    return ip not in malicious_ips