# git 私人教程

## 背景

## 安装
####在cmd中运行git.    
安装的时候注意一点。见此教程。已安装的可以把git目录加入环境变量。    
[cmd中运行git](http://jingyan.baidu.com/article/d2b1d1029065ba5c7e37d43e.html?st=2&os=0&bd_page_type=1&net_type=2)


## 常用命令
[入门教程](https://www.youtube.com/watch?v=8oRjP8yj2Wo)，当然是官方的好，简单明了。    
- git status: check what has been done
- git add -A: add all
- git add foo.py: add certain file
- git commit -m "woo": add commit
- git push: push to origin
- git pull: fetch change from origin and merge with local
- git config: configuration


## 配置
git push的时候，总是需要用户名和密码。开始的时候，同一个用户名和密码输入不下十次，就是不成功，气死我了，后来发现是密码用错了，气死我了。这就是大妈说的重复相同的行为，期待不同的结果，关键还是对电脑啊！量变不会引起质变的，亲Lol。    

后来配置ssh，最终找到了官方帮助，谁料之前折腾太多，按教程每一步都有以外，自己挖的坑太大，索性每次输入用户名和密码。    

一段时间，感觉真烦啊，难道又要折腾？来吧，没想到柳暗花明，有其他途径，就是[caching your password!](https://help.github.com/articles/caching-your-github-password-in-git/),官方的就是好。

