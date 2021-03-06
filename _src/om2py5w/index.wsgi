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

def deleteDiary():
	keys = kv.getkeys_by_prefix('key:')
	for i in keys:
		kv.delete(i)
	return "All diary cleared!"

def guide():

	temp="Tpye in help or ? to get guide!\n"\
			+"Type in anything else to write diary!\n"\
			+"Submit to see What happened!\n"\
			+"Type in del or delete to clear all diary.(DO NOT PLEASE!)"
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
		text = guide()
	elif typein in ["delete","del"]:
		text = deleteDiary()
	else:
		writeDiary(typein,tag)
		text = readDiary()
	return template('showdiary.tpl',content=text)

@app.route('/wechat')
def checkSignature():
	token = "lyltj2010"
	timestamp =request.GET.get('timestamp',None)
	nonce = request.GET.get('nonce',None)
	signature = request.GET.get('signature',None)
	echostr = request.GET.get('echostr',None)
	mylist = sorted([token,timestamp,nonce])
	mystr = ''.join(mylist)
	
	import hashlib
	password = hashlib.sha1(mystr).hexdigest()
	if password == signature:
		return echostr
	else:
		return None
#error pages
@app.error(404)
def error404(error):
	return "Nothing here, sorry!"

application = sae.create_wsgi_app(app)