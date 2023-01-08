# made by Imène ALLOUCHE
import sys

if len(sys.argv) < 2:
    print("[-] Usage: python3 solve.py <ENCRYPTED CODE>")
    sys.exit(1)

flag = ''
ENCRYPTED_CODE = sys.argv[1:]

for i in ENCRYPTED_CODE:
    flag += chr(int(i))

print(flag)
