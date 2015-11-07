# -*- coding: utf-8 -*-
#!/usr/bin/env python
from socket import *

def history():
	f = open('diary.txt','r')
	diary = f.read()
	f.close()
	return diary

def write(data):
	f = open('diary.txt','a+')
	f.write(data+'\n')
	f.close()

def help():
	help_doc = ['Key in: ','"history" to diaplay past diary',\
	'"help" to get guide','"" to write diary','"quit" to quit'\
	'or type your diary directly.\n']

	help_doc = '\n'.join(help_doc)
	return help_doc

def main():
	s = socket(AF_INET,SOCK_DGRAM)
	host = gethostbyname(gethostname())
	port = 8888
	server_addr = (host,port)
	s.bind(server_addr)

	while True:
		print "Waiting for connection!"
		data, addr = s.recvfrom(1024)
		print "Get connected by: %s" % str(addr)

		if data == 'history':
			reply = history()
			s.sendto(reply,addr)
		elif data == 'help':
			reply = help()
			s.sendto(reply,addr)
		elif data == 'quit':
			break
		else:
			write(data)
			reply = "Diary already saved.\n"+\
			"This is what you have written:\n"+data
			s.sendto(reply,addr)

	s.close()

if __name__ == "__main__":
	main()
