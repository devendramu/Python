def new():
	newlist=[]
	for i in range (1,256):
		newlist.append([])
	return newlist

def hashkey(aMap,key):
	bucket=hash(key)%len(aMap)
	return bucket

def get_bucket(aMap,key):
	return aMap(hashkey(aMap,key))

def get_slot(aMap,key):
	



list1=new()

print hashkey(list1,'abc')
print list1



