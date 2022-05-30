import re
BASE_URL="https://github.com/chasemc/duplipy/issues/new?"

def sanitize(input):
    temp = input.replace('\r', '+').replace('\n', '+').replace(' ', '+')
#    temp = re.sub('[^A-Za-z0-9-` ]+', '', temp)
    return temp.replace("++", "+")

def create_url(title="", labels="", body=""):
    temp = f"labels={sanitize(labels)}&title={sanitize(title)}&body={sanitize(body)}"
    return f"{BASE_URL}{temp}"

