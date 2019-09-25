n=input()

for rep in range(n):

	ver,ed=map(int,raw_input().split())
	conn=[]
	lis=[]
	for i in range(ver):
		conn.append([])
		lis.append([])
		for j in range (ver):
			conn[i].append(-1)
	#for i in  conn:
		#print i


	for i in range(ed):
		u,v= map(int,raw_input().split())

		conn[u-1][v-1]=6
		conn[v-1][u-1]=6

	#for i in  conn:
		#print i
	changes=1

	rep=0
	while changes>0 and rep<ver:
		changes=0
		for i in range(ver):
			for j in range (ver):

				if conn[i][j]>5 :
					if not i in lis[j]:
						lis[j].append(i)
						lis[i].append(j)

						#print "lis i is " ,i,lis[i]
						#print "lis j is ",j,lis[j]
					for k in lis[j]:
						if (conn[k][j]==-1 or conn[k][j]>conn[i][k]+conn[i][j]) and k!=j and i!=j and i!=k:
							conn[k][j]==conn[i][k]+conn[i][j]
							conn[j][k]=conn[k][j]
							changes=1
							#print " i j k are ",i,j,k
							if not k in lis(j):
								lis[j].append(k)
								lis[k].append(j)

							#for s in  conn:
								#print s

		rep=rep+1



	st=input()
	st=st-1
	for i in range(ver):
		if i!=st:
			print conn[st][i],
	print

