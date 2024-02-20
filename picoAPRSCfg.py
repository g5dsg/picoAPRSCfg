import requests
import sys

ip = sys.argv[1]
ua = requests.Session()

for cid in range(1, 17):
    n = "S" + str(cid + 7)
    f = 145.2 + ((cid - 1) * 0.025)
    freq = f"{f:03.4f}"
    print(f"{cid} {n} {freq}")
    params = {
        "id": cid,
        "Description": n,
        "TX_frequency": freq,
        "RX_frequency": freq,
        "TxTone": 0,
        "RxTone": 0,
        "scan": "on",
    }
    result = ua.get("http://" + ip + "/", params=params)
    result.raise_for_status()
