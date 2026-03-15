import json
import requests
import time

while True:
    with open("data/channels.json") as f:
        channels = json.load(f)

    working = []

    for ch in channels:
        try:
            r = requests.get(ch["url"], timeout=5)
            if r.status_code == 200:
                working.append(ch)
                print("LIVE:", ch["name"])
            else:
                print("OFFLINE:", ch["name"])
        except:
            print("OFFLINE:", ch["name"])

    with open("data/live_channels.json","w") as f:
        json.dump(working,f,indent=2)

    print("Updated live channel list. Total live channels:", len(working))
    time.sleep(120)  # check every 2 minutes