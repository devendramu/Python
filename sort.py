str1=raw_input()

strst=sorted(list(str1))

dig=filter(lambda x:ord(x)>47 and ord(x)<58,strst)
odd=filter(lambda x:int(x)%2!=0,dig)
even=filter(lambda x:int(x)%2==0,dig)
sml=filter(lambda x:ord(x)>=97 and ord(x)<=122,strst)
cap=filter(lambda x:ord(x)>=65 and ord(x)<=97,strst)


def prn(x):
	
	print "\b%s" %x,
	
map (prn,sml)
map (prn,cap)
map (prn,odd)
map (prn,even)

