# CLI 私人教程

### 背景
据说程序员跟电脑打交道都是用CLI，让人禁不住想试一试。

### Powershell
Windows党先用Powershell吧。   
####特点
- 交互与脚本：例如可以打开ipython，及时交互；也可以run hello.py直接运行脚本。
- 命令规则：动词+名词，如New-Item， Get-Help。
- 兼容cmd：shell里命令叫cmdlet，同时为cmd命令起了alias，可以get-alias查看。
- [入门教程](http://www.cnblogs.com/chsword/archive/2011/10/17/PowerShell_2.html)

###常用命令
- cd ：目录操作(利用tab补全)
- cd.. ：返回上一级
- cd\ :返回跟目录
- dir/ls ：列举文件
- rm ：remove

###问题
如何在powershell中运行sublime(如命令subl)？

### 其他
####在git bash中运行sublime  
[Udacity教程](https://www.udacity.com/wiki/ud775/sublime)
