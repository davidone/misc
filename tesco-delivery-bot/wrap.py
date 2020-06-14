#!/usr/local/bin/python3.7

import subprocess
import os
import http.client, urllib

PO_API_TOKEN = ""
PO_USER_KEY = ""
NODE_BIN = "/usr/local/bin/node"


class cd:
    """Context manager for changing the current working directory"""

    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def define_po_keys():
    global PO_API_TOKEN, PO_USER_KEY
    try:
        PO_API_TOKEN = os.environ["PO_API_TOKEN"]
        PO_USER_KEY = os.environ["PO_USER_KEY"]
    except KeyError as err:
        print(
            f"Error: {err}. Check if your environment defines PO_API_TOKEN and PO_USER_KEY"
        )
        exit(1)
    if not PO_API_TOKEN or not PO_USER_KEY:
        print(f"Error: PushOver token or key are empty.")
        exit(1)


def check_tesco() -> list:
    with cd("~/delivery-slot-bot"):
        result = subprocess.run(
            [NODE_BIN, "delivery-slots.js"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    if result.stderr:
        print(f"ERROR: {result.stderr}")
        return []

    result_list = result.stdout.split("\n")
    print(result_list)


def process_tesco(t_list) -> str:
    return "ok world"


def send_po(message) -> bool:
    if not message:
        print("message is emtpy")
        return True

    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request(
        "POST",
        "/1/messages.json",
        urllib.parse.urlencode(
            {"token": PO_API_TOKEN, "user": PO_USER_KEY, "message": message,}
        ),
        {"Content-type": "application/x-www-form-urlencoded"},
    )
    res = conn.getresponse()
    if res.status not in range(200, 300):
        return False
    return True


if __name__ == "__main__":
    define_po_keys()
    res_tesco = check_tesco()
    message = process_tesco(res_tesco)
    send_po(message)
