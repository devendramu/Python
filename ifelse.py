
n=input()
print "ns is %d" %n
a=n%2
print a
if n%2==0:
	print "Weird"
	print "n%2"
elif n>=2 and n<=5:
	print "Not Weird"
	print "n>=2 and n<=5:"
elif n>=6 and n<=20:
	print "Weird"
	print "n>=6 and n<=20"
else:
	print "Not Weird"
