from sys import argv

script,file_name = argv

print "filename is ",file_name
filep=open(file_name)
print filep.read()

print "enter a filename ",
file_name= raw_input("?")
filep=open(file_name,'w')
filep.truncate()

print " enter lines",
line1=raw_input('line 1 ?')
line2=raw_input('line 2 ?')

filep.write(line1 + '\n' +line2+ '\n test')
filep.write(line2)