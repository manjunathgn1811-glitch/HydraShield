import json

sample_feed = [
    "45.10.22.10",
    "91.22.11.4",
    "101.10.10.1"
]

def update_feed():

    with open(
        "threat_feeds/feed.json",
        "w"
    ) as f:

        json.dump(
            sample_feed,
            f
        )

    return True