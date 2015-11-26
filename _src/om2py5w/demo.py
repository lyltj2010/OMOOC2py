# -*- coding: utf-8 -*-
#!/usr/bin/env python
from bottle import *
import sae

app = Bottle()
'''
@app.route('/')
def hello():
	return "Hey, dude!"
'''
def readDiary():
	with open('diary.txt','r') as f:
		text = f.read()
	return text 

def writeDiary(typein):
	with open('diary.txt','a+') as f:
		f.write(typein+'\n')

def guide():

	temp="Tpye in help or ? to get guide!\n"\
			+"Type in anything else to write diary!\n"\
			+"Submit to see What happened!" 
	return temp

@app.route('/')
def show():
	text = readDiary()
	return template('showdiary.tpl',content=text)

@app.route('/',method='POST')
def new():
	typein=request.forms.get('typein')
	if typein in ["help","?"]:
		text=guide()
	else:
		writeDiary(typein)
		text = readDiary()
	return template('showdiary.tpl',content=text)

#error pages
@app.error(404)
def error404(error):
	return "Nothing here, sorry!"

'''
if __name__ == "__main__":
    debug(True)
    run(host='localhost',port=8080,reloader=True)
'''

application = sae.create_wsgi_app(app)