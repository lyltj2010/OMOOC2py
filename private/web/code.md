```python
import webbrowser
from sys import argv

script, website = argv

def addWeb(dic):
	'''add new interesting website'''

	print "Please input webname and url"
	web_name = raw_input("webname: ")
	web_url = raw_input("weburl: ")
	dic[web_name] = web_url

	f = open('webpool.txt','w')
	f.write(str(dic))
	f.close()

def delWeb(dic):
	'''delete outdated website'''

	print "Please input webname you wanna delete."
	web_name = raw_input("webname: ")
	del dic[web_name]

	f = open('webpool.txt','w') 
	f.write(str(dic))
	f.close()

def listAll(dic):
	'''show what website you have saved'''
	for item in dic:
		print item.title()

def openWeb(dic):
	'''open interested webpage'''
	try:
		url = dic[website]
		webbrowser.open(url, new = 2)
	except KeyError:
		print "Sorry, this site is not included in your webpool!"

def loadPool():
	'''load saved websites'''
	f = open('webpool.txt','r')
	dic = eval(f.read())
	return dic
	f.close()

def search():
	'''use google to search'''
	url = "http://google.com/#q="
	terms = raw_input("Enter search query: ")
	terms = terms.replace(" ","+")

	webbrowser.open(url+terms,new=2)

def help1():
	'''help doc'''
	text = ['1.Enter website name to open.',\
	'2.Enter "add" to add new website.',\
	'3.Enter "del" to delete old website.',\
	'4.Enter "search" or "s"to search with google.',\
	'5.Enter "help" or "?" to get guide.',\
	'6.Enter "dir" or "ls" to show what you have saved']
	text = '\n'.join(text)
	print text

if __name__ == "__main__":
	
	dic =	loadPool()

	if website == 'add':
		addWeb(dic)
	elif website == 'del':
		delWeb(dic)
	elif website in ['ls','dir']:
		listAll(dic)
	elif website in ['s','search']:
		search()
	elif website == 'help':
		help1()
	else:
		openWeb(dic)
```