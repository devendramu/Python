N=input()
data={}

#for i in range(0,N):


for i in range(0,N):
	inp=raw_input()
	#print inp

	marks=inp.split()
	#print words
	key=marks.pop(0)
	#print key
	
	data[key]=marks
	#inp.pop
#print data

keytest=raw_input()
marks=data[keytest]
avg=(int(marks[0])+int(marks[1])+int(marks[2]))/3.0
#avg=round(avg,2)
print "%.2f" %avg
#print maths ,chem

