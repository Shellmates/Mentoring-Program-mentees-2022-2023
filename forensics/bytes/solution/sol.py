all_bytes= eval(open("bytes.txt","r").read())

#empty list
l= [b"_" for i in range(len(all_bytes))]
for i in all_bytes:
	l[i[0]]=i[1].to_bytes(1,byteorder='big')


open("solution","wb").write(b"".join(l))
