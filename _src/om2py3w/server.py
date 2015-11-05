# -*- coding: utf-8 -*-
#!/usr/bin/env python
from socket import *

def history():
	f = open('diary.txt','r')
	diary = f.read()
	f.close()
	return diary

def write():
	content = raw_input("Any thing want to share?\n>>")
	f = open('diary.txt','a+')
	f.write(content)
	f.close()

def help():
	help_doc = "Keyin 'history' to show past diary,\
	'quit' to quit, 'help' for help document and \
	anything else to enter writing mode."
	print help_doc

s = socket(AF_INET,SOCK_DGRAM)
host = gethostbyname(gethostname())
port = 8888
server_addr = (host,port)
s.bind(server_addr)

while True:
	print "Waiting for connection!"
	data, addr = s.recvfrom(1024)
	if data == 'history':
		print history()
	elif data == 'help':
		help()
	elif data == 'quit':
		break
	else:
		write()

s.close()

