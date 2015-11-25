##Show your think
####首先要能打开浏览器
- google发现用到```import webbrowser```
```python
def openWeb(dic):
	'''open interested webpage'''
	try:
		url = dic[website]
		webbrowser.open(url, new = 2)
	except KeyError:
		print "Sorry, this site is not included in your webpool!"
```
####需要一个收藏夹
- 应该用字典key & value最match需求
- 首次尝试，更新w.py内不变量，企图让其更新自身Lol.
- 尝试利用外部webpool.txt
- 如何读取为字典？google发现可以用```eval()```函数
```python
def loadPool():
	'''load saved websites'''
	f = open('webpool.txt','r')
	dic = eval(f.read())
	return dic
	f.close()
```
- 如何写入新的网址收藏？```write```折腾好久，之前尝试用```f.seek()```写入特定位置，但添加删除等反复改变，最终放弃，百思不得其姐，偶然想到```f.write(str(dic))```
```python
def addWeb(dic):
	'''add new interesting website'''

	print "Please input webname and url"
	web_name = raw_input("webname: ")
	web_url = raw_input("weburl: ")
	dic[web_name] = web_url

	f = open('webpool.txt','w')
	f.write(str(dic))
	f.close()
```

读写搞定，其余的就小case。

####如何给关键词直接搜索
google发现youtube有个小视频，代码很简单。
```python
def search():
	'''use google to search'''
	url = "http://google.com/#q="
	terms = raw_input("Enter search query: ")
	terms = terms.replace(" ","+")

	webbrowser.open(url+terms,new=2)
```
