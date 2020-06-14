import http.client, urllib

PO_API_TOKEN = ""
PO_USER_KEY = ""

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def check_tesco() -> list:
  with cd("/path/delivery-slot-bot"):
    result = subprocess.run(["node", "delivery-slots.js"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  if result.stderr:
    print(f"ERROR: {result.stderr}")
    return []

  result_list = result.stdout.split('\n')
  print(result_list)


def process_tesco(t_list) -> str:
  pass


def send_po(message) -> bool:
  if not message:
    print("message is emtpy")
    return True
  conn = http.client.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
      "token": PO_API_TOKEN,
      "user": PO_USER_KEY,
      "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
  res = conn.getresponse()
  if (res.status not in range(200, 300)):
    return False
  return True


if __name__ == "__main__":
