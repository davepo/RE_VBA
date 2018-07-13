import os
import ctypes

def Mid(data, start, length):
	return data[start : (start+length)]			

def Val(data):
	if data[0] == '&' and data[1] == 'H':
		data = data[2:]
		return int(data, 16)
	y=0
	new_str=""
	num_list=['0','1','2','3','4','5','6','7','8','9']
	for x in data:
		for i in num_list:
			if x == i:
				new_str=new_str+x
	n=len(new_str)
	count=n
	res=0
	for z in range(n):
		y=0
		for i in num_list:
			if new_str[z] == i:
				w=y
				mult=1
				count=count-1
				for j in range(count):
					mult=mult*10
				res=res+(w*mult)
			y=y+1
	return res
	
def Len(data):
	return len(data)
	
def Chr(data):
	return unichr(data)
	
def Asc(data):
	return ord(data)

def Environ(env_var):
	return os.environ[env_var]

def OpenForBinaryAccess(path):
	return open(path, "wb")

def MsgBox(message):
	ctypes.windll.user32.MessageBoxW(0, message, "Message", 0)

#def SetAttr(path, val):

#def ObjectRun(file)
