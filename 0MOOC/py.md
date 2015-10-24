# Python 私人教程

## 背景
大妈云：
> 在开始学习 Python 之前,需要先配置好 Python 的常用环境, 这可能是个"先有鳮,还是先有蛋"的事儿, 但是,就是这么任性!

## PIP
####安装pip
官网上给的安装代码[get-pip.py](https://bootstrap.pypa.io/get-pip.py)，拷贝来建立一个py文件。
在cmd输入如下代码

````python get-pip.py````

biubiu，搞定啦。

####安装第三方模块
之后就可以任性安装卸载其他模块。
- 安装
````pip install some-package-name````
- 卸载
````pip uninstall some-package-name````


####不够给力？
给你个wiki
[PIP](https://en.wikipedia.org/wiki/Pip_(package_manager))

##Ipython
当然，还可以任性地把Ipython安装了。

````pip install ipython````    
在cmd或powershell打开ipython时会出现一堆提示，这是安装一下pyreadline。
````pip install pyreadline````    
之后就可以任性地用Ipython。    
- 命令行：可以直接交互
- 脚本：可以直接````run hello.py````,在也不用反复退出了。