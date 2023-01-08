import base64
import sys


if len(sys.argv) != 2:
    print("[-] Usage: pyhton3 solve.py <ENCRYPTED TEXT>")
    sys.exit()

ENCRYPTED_TEXT = sys.argv[1]


# for the decryption
base64_bytes = ENCRYPTED_TEXT.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("ascii")

print(sample_string)
