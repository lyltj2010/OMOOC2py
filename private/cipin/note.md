####统计词频
看见阿赖同学小知识里面dict.get()方法的介绍,竟然几行代码就能统计文档的词频，赶紧偷过来。  
[dict.get()和dict[key]区别](http://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey)
```python
doc =  \
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
count = {}
for word in doc.split():
	#找不到可以给默认值
	count[word] = count.get(word,0)+1
print count
#结果返回一个词典
{'Beautiful': 1, 'Python,': 1, 'Explicit': 1, 'than': 4, 'complex.': 1, 'Simple': 1, 'of': 1, 'is': 4, 'Zen': 1, 'Peters': 1, 'better': 4, 'Tim': 1, 'Complex': 1, 'ugly.': 1, 'implicit.': 1, 'The': 1, 'by': 1, 'complicated.': 1}
```