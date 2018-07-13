import os

def Mid(data, start, length):
	return data[start : (start+length)]			

def Val(data):
	if data[0] == '&' and data[1] == 'H':
		data = data[2:]
		return int(data, 16)
	y=0
	nst=""
	dlist=['0','1','2','3','4','5','6','7','8','9']
	for x in data:
		for i in ldlist:
			if x == i:
				nst=nst+x
	n=len(nst)
	dcont=n
	acum=0
	for z in range(n):
		y=0
		for i in dlist:
			if nst[z] == i:
				d=y
				mult=1
				dcont=dcont-1
				for j in range(dcont):
					mult=mult*10
				acum=acum+(d*mult)
			y=y+1
	return acum
	
def Len(data):
	return len(data)
	
def Chr(data):
	return unichr(data)
	
def Asc(data):
	return ord(data)

def Environ(env_var):
	return os.environ[env_var]

#def SetAttr(path, val):

def OpenForBinaryAccess(path):
	return open(path, "wb")
