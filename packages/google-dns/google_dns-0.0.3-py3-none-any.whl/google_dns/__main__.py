import logging
import time
from tkinter import E

import requests

from google_dns import cfg


def get_ip():
    url = cfg.url
    headers = {
        "content-type": "application/json",
        "Accept-Charset": "UTF-8",
        "Authorization": f"Basic {cfg.authorization}",
        "Cookie": cfg.cookie,
    }
    try:
        # Send request
        data = requests.get(url, headers=headers).text
        # Parse the ip
        reg = "WAN側IPアドレス"
        lines = data.split(reg)
        ip = lines[1].split("td>")[1].split("<")[0]
        return ip
    except requests.exceptions.ConnectionError as e:
        return None


if __name__ == "__main__":
    try:
        my_ip = get_ip()
        assert my_ip is not None
        for host in cfg.hostnames:
            url = (
                f"https://{host.google_id}"
                f":{host.google_password}@domains.google.com/nic/update?"
                f"hostname={host.hostname}&"
                f"myip={my_ip}"
            )
            logging.warning(requests.get(url).text)
        time.sleep(3600)
    except:
        pass
