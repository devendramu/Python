n=input()
distel=0
mylis=[]
for i in range (n):
	mylis.append(raw_input())


#print "mylist is %r" %mylis
outlist=[]
while len(mylis)!=0:
	i=mylis.pop(0)
#	print "i is %s " %i

#	print "distel = " , distel
#	print "mylis after pop ",mylis

	outlist.append(1)
#	print "outlist is ",outlist


	itemnum=0
	for j in mylis:

		if i==j:
#			print "match found at ",itemnum

			outlist[distel]=outlist[distel]+1
			del mylis[itemnum]
#			print outlist
#			print mylis
		itemnum=itemnum+1		

	distel=distel+1

print distel
for i in outlist
	print i
