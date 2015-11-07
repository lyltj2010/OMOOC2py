# -*- coding: utf-8 -*-
#!/usr/bin/env python
from socket import * #for socket
import sys #for exit

try:
	s = socket(AF_INET,SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket.'
	sys.exit()

host = gethostbyname(gethostname())
port = 8888
server_addr = (host,port)

while True:
	msg = raw_input('Enter message to send: ')
	#send the msg.
	s.sendto(msg,server_addr)

	if msg == 'quit':
		break
	#receive data from client
	reply, addr = s.recvfrom(1024)
	print 'Server reply:\n'+ reply