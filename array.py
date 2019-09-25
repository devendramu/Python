import numpy
m,n,p=raw_input().split()
m=int(m)
n=int(n)
p=int(p)

array1=[]
array2=[]
item=[]
for i in range (m):
	item = raw_input().split()
	item1=map(int,item)
	array1.append(item1)

for i in range(n):
	item = raw_input().split()
	item1=map(int,item)
	array2.append(item1)

print numpy.concatenate((array1,array2))



