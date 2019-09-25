tc=input()

for i in range(tc):

	n=input()
	mylist=raw_input().split()

	if n==1:
		print "Yes"
	else:

		left=int(mylist.pop(0))
		right=int(mylist.pop(-1))
	#	print "left =%d right=%d  %s" %(left,right,mylist)
		
		if left<right:
				num=right
		else:
			num=left
	#	print "left =%d right=%d num=%d" %(left,right,num)

		while mylist!=[] and num>=left and num>=right:
	#		print "left =%d right=%d num=%d" %(left,right,num)

			if left>right:
				num=left
				left=int(mylist.pop(0))
	#			print "left =%d right=%d num=%d   %s"%(left,right,num,mylist)
			else:
				num=right
				right=int(mylist.pop(-1))
	#			print "left =%d right=%d num=%d    %s" %(left,right,num,mylist
					

	if mylist==[] and num>=left and num>=right:
		print "Yes"
	else:
		print "No"
