


def findconn(row,connc):
	global lis

	lis.append(row)
	conrow=[]
	for i in range(len(connc[row])):
		##print("in fun with i=  ",i)
		if connc[row][i]!=-1 and i not in lis:
			findconn(i,connc)
			
	#print lis

	return len(lis)


irem=0
global conn
global st
global lis
connc=[]
conn=[]
ver,ed=map(int,raw_input().split())
#lis=[]
for i in range(ver):
	conn.append([])
	#lis.append([])
	for j in range (ver):
		conn[i].append(-1)


for i in range(ed):
	u,v= map(int,raw_input().split())
	conn[u-1][v-1]=6
	conn[v-1][u-1]=6
#for y in range(ver):
	#print conn[y]

for i in range(ver):
	for j in range(ver):
		if conn[i][j]!=-1:
			#print "trying to remove ",i,j
			connc=conn
			
			connc[i][j]=-1
			connc[j][i]=-1
			irem=irem+1
			lis=[]
			##print conn
			#print ("calling findconn with folloing connc")
			#for y in range(ver):
				#print connc[y]
			nc=findconn(i,connc)
			#print nc
			if nc%2!=0:
				irem=irem-1
				
				conn[i][j]=6
				conn[j][i]=6
			else:
				print " remved ",i,j
			#print conn
print conn
print irem