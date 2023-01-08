import base64
import sys


if len(sys.argv) != 2:
    print("[-] Usage: pyhton3 solve.py <PLAIN TEXT>")
    sys.exit()

PLAIN_TEXT = sys.argv[1]


#for the encrytion
encrypted_text_bytes = PLAIN_TEXT.encode("ascii")
base64_bytes = base64.b64encode(encrypted_text_bytes)
base64_string = base64_bytes.decode("ascii")

print(base64_string)
