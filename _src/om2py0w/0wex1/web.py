import webbrowser
from sys import argv
script, website = argv

def AddWeb():
	print "Please input webname and url"
	web_name = raw_input("webname: ")
	web_url = raw_input("weburl: ")
	f = open('webpool.txt','r+')
	f.seek(-1,2)
	combo = '\"'+web_name+'\"'+':'+'\"'+web_url+'\"'+','+'\n'+'}'
	f.write(combo)
	f.close()

def DelWeb():
	pass

def OpenWeb(website):
	f = open('webpool.txt','r')
	dic = eval(f.read())
	f.close()

	url = dic[website]
	webbrowser.open(url, new = 2)

if website=="update":
	AddWeb()
else:
	OpenWeb(website)

'''
dict_1 = {"baidu":"http://www.baidu.com",
"google":"https://www.google.com",
"github":"https://github.com/lyltj2010?tab=repositories",
"gitbook":"https://www.gitbook.com/book/yongle/-python-/details",
"dashijian":"http://v.qq.com/detail/3/30406.html",
"bizhan":"http://www.bilibili.com/",
"howdy":"https://howdy.tamu.edu/cp/home/displaylogin",
"zhimaxing":"http://www.iomooc.com/pages/login.html"}

url = dict_1[website]
webbrowser.open(url, new = 2)
'''

