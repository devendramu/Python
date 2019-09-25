n=input()
lis=raw_input().split()
lis=list(map(int,lis))

lis=sorted(lis)
a=set(lis)
lis=list(a)

#print lis
print lis[n-2]