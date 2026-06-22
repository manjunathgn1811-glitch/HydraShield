from datetime import datetime

def honeypot_trigger(ip):

    return {
        "attacker": ip,
        "event": "honeypot_hit",
        "time": str(datetime.now())
    }