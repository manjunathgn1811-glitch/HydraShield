blocked_ips = {
    "192.168.1.100",
    "10.0.0.50"
}

def check_ip(ip):
    if ip in blocked_ips:
        return False
    return True

def block_ip(ip):
    blocked_ips.add(ip)