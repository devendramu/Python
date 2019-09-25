strg=raw_input()
lis=[]
lis=list(strg)

ind=0
print lis
for i in lis:
	if ord(i)>=65 and ord(i)<=90:
		i=chr(ord(i)+32)
		lis[ind]=i
		ind=ind+1
	elif ord(i)>=97 and ord(i)<=122:
		i=chr(ord(i)-32)
		lis[ind]=i
		ind=ind+1
	else:
		lis[ind]=i
		ind=ind+1

strg=''.join(lis)
print strg