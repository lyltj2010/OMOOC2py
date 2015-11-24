# -*- coding: utf-8 -*-
#!/usr/bin/env python

from bottle import *

def readDiary():
	with open('diary.txt','r') as f:
		text = f.read()
	return text 

def writeDiary(typein):
	with open('diary.txt','a+') as f:
		f.write(typein+'\n')

@route('/diary')
def show():
	text = readDiary()
	return template('showdiary.tpl',content=text)

@route('/diary',method='POST')
def new():
	typein=request.forms.get('typein')
	writeDiary(typein)
	text = readDiary()
	return template('showdiary.tpl',content=text)

#error pages
@error(404)
def error404(error):
	return "Nothing here, sorry!"

if __name__ == "__main__":
    debug(True)
    run(host='localhost',port=8080,reloader=True)
