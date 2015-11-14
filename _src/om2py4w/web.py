# -*- coding: utf-8 -*-
#!/usr/bin/env python

from bottle import *

@get('/diary')
def diary():
	f = open('diary.txt','r')
	content = f.read()
	f.close()
	return template('showdiary.tpl',content=content)

@get('/newdiary')
def newDiary():
	return '''
		<form action="/newdiary" method="post">
			Diary: <input name="content" type="text" />
        </form>
		'''
@post('/newdiary')
def do_newDiary():
	content=request.forms.get('content')
	return content

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username=='lyl' and password=='123':
        return "<a href='http://localhost:8080/diary'>Click me.</a>"
    else:
        return "<p>Login failed.</p>"
#error pages
@error(404)
def error404(error):
	return "Nothing here, sorry!"

if __name__ == "__main__":
    debug(True)
    run(host='localhost',port=8080,reloader=True)
