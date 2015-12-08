##问题先行
- 代码码哪
- 接口是啥
- 什么关系(用户-服务端-我)
- XML是什么鬼
- 如何数据本地备份

##学习
- [XML概念w3schools](http://www.w3schools.com/xml/xml_whatis.asp),第一阶段了解XML是什么鬼就行，不要借钻研之名，跳出任务范畴。  
- [Python相关模块](https://docs.python.org/2.7/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.items)，如何处理XML格式的数据  
- [乱入一下Http请求方法](http://blog.csdn.net/mfe10714022/article/details/39692305)，对Get,Post,put,delete这几个概念不是很理解，看后发现原理对应对资源的查、改、增、删。比如读新闻，发评论就分别对应Get和Post。  
- [微信接入指南,第一遍完全不懂](http://mp.weixin.qq.com/wiki/16/1e87586a83e0e121cc3e808014375b74.html),那就看三遍，然后research哪里不懂。  
- [廖雪峰参考](http://www.liaoxuefeng.com/article/0013900476318564121d01facf844cba508396f95d9bb82000)
##Try
认证代码写完后，就是通不过，就是通不过，就是通不过。然后就搜，发现可能是sae**没有实名验证**，导致token验证失败，验证一下去！！！
```python
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
```
结果证明是这样的。