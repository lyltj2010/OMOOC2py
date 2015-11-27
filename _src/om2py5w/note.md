##问题先行
- 代码写哪？跟sae什么关系？
- 和bottle怎么连接？如何在sae中运用
- 如何本地完成，然后再部署？
- 怎么用CLI与其联系？
- 数据如何管理？
##学习
- [Paas是什么鬼](https://en.wikipedia.org/wiki/Platform_as_a_service)  
- [新浪云](http://www.sinacloud.com/doc/sae/python/index.html)

##sae
安装```pip install sae-python-dev```

##Try
####理应寻找Quickstart
> 目标是quickstart，然后keep rolling.  

1、[helloworld](http://www.sinacloud.com/doc/sae/python/tutorial.html#id2)  
2、发现需要svn  
3、[使劲戳这安装svn](http://www.cnblogs.com/armyfai/p/3985660.html)    
4、嗯，quickstart了，不过cmd需要从svn打开才管用，不知道为啥。  
5、后来发现好像不需要...
####本地测试
[答案在这](http://www.sinacloud.com/doc/sae/python/tools.html)，sae文档理应有这些基本guide。  
1、```pip install sae-python-dev```  
2、进入开发目录(index.wsg和config.yaml所在处),运行```dev_server.py```  
3、访问http://localhost:8080即可  
####部署
1、部署```more config.yaml```(查看配置信息) ```saecloud deploy```(接受可选参数，应用代码目录)   
2、接口好像弄个```app=Bottle()```就ok了，嗯，再看看同侪的代码，学习一下去。  
3、so far so good.

####数据问题
发现竟然还是用本地txt做数据库，Lol.  
用kvdb创建数据解决之。  
赶紧下周吧，课程都要结束了，下周也要final了，加油！
