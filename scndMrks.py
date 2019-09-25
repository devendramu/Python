nstds=input()
names=[]
marks=[]

for i in range (nstds):
#	print "input name %d" %i
	names.append(raw_input())
	marks.append(input())

for i in range (nstds):
	j=i
	while(j<nstds):
		if marks[i]<marks[j]:

			temp=marks[i]
			marks[i]=marks[j]
			marks[j]=temp

			temp=names[i]
			names[i]=names[j]
			names[j]=temp
		j=j+1

print marks
print names
studlist=[]
if nstds!=2:
	while marks[nstds-1]==marks[nstds-2]:
		nstds=nstds-1

if nstds==2:
	print names[0]
else:
	while True:
		studlist.append(names[nstds-2])

		if nstds==2 or marks[nstds-2]!=marks[nstds-3]:
			break
		nstds=nstds-1

studlist=sorted(studlist)
for i in studlist:
	print i