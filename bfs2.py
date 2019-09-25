#from __future__ import print_function



conn=[]

def findconn(row,conn):
	conrow=[]
	for i in range(len(conn[row])):
		##print("in fun with i=  ",i)
		if conn[row][i]!=-1:
			conrow.append(i)

	#print(conrow)
	return conrow


def depret(caller,lis,depth):
	global conn
	global st
	lis.append(caller)

	#print (" called by %d with lis and dep as " %st ,lis, depth)
	#for i in range (4):
		#print (conn[i])
	
	
	#print ("lis is ",lis)
	conrow=findconn(caller,conn)
	for i in conrow:
		if not i in lis:
			if conn[st][i]==-1 or conn[st][i]>(depth*6):
				conn[st][i]=depth*6
			depret(i,lis,depth+1)

	




n=input()
for itr in range (n):
	conn=[]
	global st
	ver,ed=map(int,raw_input().split())
	lis=[]
	for i in range(ver):
		conn.append([])
		lis.append([])
		for j in range (ver):
			conn[i].append(-1)


	for i in range(ed):
		u,v= map(int,raw_input().split())

		conn[u-1][v-1]=6
		conn[v-1][u-1]=6

	#for i in range(ver):
		#print (conn[i])


	st=input()
	lis=[]
	st=st-1
	depret(st,lis,1)

	for i in range (ver):
		if i!=st:
			print conn[st][i],
	print