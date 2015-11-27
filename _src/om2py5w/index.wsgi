# -*- coding: utf-8 -*-
#!/usr/bin/env python
from bottle import *
import sae
import sae.kvdb

app = Bottle()
kv = sae.kvdb.Client()

def readDiary():
	
	text = []; tag = []
	for i in kv.get_by_prefix('key:'):
		# here i is tuple access by index
		text.append(i[1]["content"])
		tag.append(i[1]["tag"])
	log = []
	for j in range(len(text)):
		log.append('Diary: '+text[j]+'\n'+'Tag: '+tag[j])
	return '\n'.join(log)

def writeDiary(content,tag):
	diary = {"content":content,"tag":tag}
	# diary includes content and tag
	# (dict) access by key
	kv.set('key:'+tag, diary)

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
	tag=request.forms.get('tag').replace(' ','')
	if typein in ["help","?"]:
		text=guide()
	else:
		writeDiary(typein,tag)
		text = readDiary()
	return template('showdiary.tpl',content=text)

#error pages
@app.error(404)
def error404(error):
	return "Nothing here, sorry!"

application = sae.create_wsgi_app(app)