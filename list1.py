N=input()
data=raw_input()
list1=data.split()
for i in range (N):
	list1[i]=int(list1[i])


print hash(tuple(list1))

	