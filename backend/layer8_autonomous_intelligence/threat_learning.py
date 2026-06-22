import json

THREAT_FEED_FILE = "threat_feeds/feed.json"

def load_feed():

    try:

        with open(
            THREAT_FEED_FILE,
            "r"
        ) as f:

            return json.load(f)

    except:

        return []

def check_feed(ip):

    threats = load_feed()

    return ip in threats