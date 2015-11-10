# -*- coding: utf-8 -*-
#!/usr/bin/env python

from bottle import *

@route('/diary')
def diary():
	f = open('diary.txt','r')
	content = f.read()
	f.close()
	return content

#error pages
@error(404)
def error404(error):
	return "Nothing here, sorry!"

if __name__ == "__main__":
    debug(True)
    run(host='localhost',port=8080,reloader=True)
