x=input()
y=input()
z=input()
N=input()

sx1=[]
sx1=[map(int,chr(i+48).split()+chr(j+48).split()+chr(k+48).split()) for i in range(x+1)  for j in range(y+1) for k in xrange(z+1) if i+j+k !=N]

#sx1=[i for i in range(10) if i<3s]



#sy=[i for i in range(y)]




print sx1