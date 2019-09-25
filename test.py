import email.utils
#n=input()
val="name <user@email.com>"
parval=email.utils.parseaddr(val)
print("parval is " + str(parval)+ " type is " + str(type(parval)))
print (parval[1])
