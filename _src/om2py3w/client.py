# -*- coding: utf-8 -*-
#!/usr/bin/env python
from socket import *

s = socket(AF_INET,SOCK_DGRAM)
host = gethostbyname(gethostname())
port = 8888
server_addr = (host,port)

text = 'history'
s.sendto(text,server_addr)