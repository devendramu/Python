import re
p=input()

res="-1"
m = re.findall('[A-Za-z0-9]',p)
#print (m)
prev='~'
while (m):
    char=m.pop(0)
    #print (char)
    #print (m)
    if prev==char:
        res=char
        break;
    prev=char
print (res)