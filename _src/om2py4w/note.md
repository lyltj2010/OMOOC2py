##岩钉
>日记就像岩钉，  
不但记录你成长的过程，  
还防止你被摔死！  
Lol.  
####记录探索过程
所谓的思维训练，思维成长不就这样？不断地猜想，不断地反驳，不断地解决问题。  
####入门
[Bottle](http://bottlepy.org/docs/dev/tutorial.html#generating-content),直奔官方教程的Quickstart,MVP就开始rolling了.

- 构思程序最基本功能：读日记、写日记、帮助文件。先来三个函数：
```python
def readDiary():
	pass
def writeDiary():
	pass
def helpDoc():
	pass
```
- 读用get，最基本
```python
@route('/diary')
def diary():
	text = readDiary()
	return template('showdiary.tpl',content=text)
```
- template是什么鬼，需要html语言基本知识  
[十分钟入门](http://www.w3schools.com/html/default.asp)

```python
<head>
  <title>This is my diary website.</title>
  <meta charset = "utf-8">
</head>

<body>

<h2>Hey dude, anything wanna share today? </h2>
<p>Just <b>feel free</b> to tell me!</p>
<pre><p>日记就像岩钉，
不但记录你成长的过程，
还防止你被摔死！
Lol.</p></pre>

<p>以下是往期日记：<hr>
<pre>
<textarea rows="40" cols="120">{{content}}</textarea>
</pre>
</p>

</body>
```

- wonder够了，进入post，writediary  
关键是post，form的用法，实现用户通过网页与server交互。
```python
#tpl里面form代码
<form action="/diary" method="post">
Write diary here:<br>
	<input type="text" style="width:300px; height:35px" name="typein"/>#把用户input赋值给name typein
	<input type="submit" value="Submit"/>#Value显示在网页上
</form>
```

```python
#web.py配套代码
@route('/diary',method='POST')#用POST
def new():
	typein=request.forms.get('typein')#就是为了typein这一项！
	writeDiary(typein)
	text = readDiary()
	return template('showdiary.tpl',content=text)
```
####debug
中间有bug，发现后笑哭。POST时，tpl里面form已经写好，但是request.forms.get()就是写不到本地文件，出错，file object没有wirte属性。从request排查，用type(typein)和print typein都没发现问题，必然是写入的问题，然后发现是writeDiary函数里f.write写成f.wirte了，**typo啊**！

####吐槽自己
大妈**告诉你不要憋大招**。。。你看看你憋的落下两周课程有木有。让MVP持续rolling就行，算了，原谅你这一次。继续下周！