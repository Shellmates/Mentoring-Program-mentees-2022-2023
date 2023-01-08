import sys

if len(sys.argv) != 2:
    print("[-] Usage: python3 solve.py <ENCRYPTED HEX CODE>")
    sys.exit()


hexstring = sys.argv[1]
a_string = bytes.fromhex(hexstring)
a_string = a_string.decode("ascii")
print(a_string)
