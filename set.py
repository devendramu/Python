ele1=input()
lis1=raw_input().split()
lis1=list(map(int,lis1))


ele2=input()
lis2=raw_input().split()
lis2=list(map(int,lis2))


set1=set(lis1)
set2=set(lis2)
diff=set()

diff=set1.difference(set2)
diff2=set2.difference(set1)
diff.update(diff2)

diff=sorted(diff)


for x in diff:
	print x
print diff