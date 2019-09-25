import re
import email.utils
#str=input()
#n=input()
n=int(input())
for i in range(n):

    val=input()
    parval=email.utils.parseaddr(val)
    #print("parval is " + str(parval)+ " type is " + str(type(parval)))
    str= (parval[1])
    #print ("str is "+str)
    #str="abc.coa.aw"
    if ((bool(re.search(r'^[a-zA-Z]+[\w\.-]*\@[a-zA-Z]+\.[a-zA-Z][a-zA-Z][a-zA-Z]?$',str)))):
        print(email.utils.formataddr(parval))

