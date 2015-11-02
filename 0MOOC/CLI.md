# CLI 私人教程

### 背景
据说程序员跟电脑打交道都是用CLI,让人禁不住想试一试.

### cmd
Windows党先用cmd吧  
####特点
- 交互与脚本:例如可以打开ipython，及时交互；也可以run hello.py直接运行脚本。

- 快:我这用了五年的破电脑，cmd也是秒开，呵呵。

###常用命令
- cd: similar to pwd, current directory
- cd: change directory to 
- cd..: back one level
- cd\: back to root
- dir: list all the files
- mkdir: new folder
- more: display contents of file
- move: used to move file or rename
- copy: eg copy foo.py bar.py
- del: delete
- cls: clear windows

###如何在cmd中运行sublime(如命令subl)?
I would say that adding Sublime's installation directory to PATH is a convenient way to enable Sublime launched from cmd. For me:    
Simply Right click on Computer. Select properties then click on "Advanced System Settings". From there Go to Environment Variables>Path and append ;C:\Program Files\Sublime Text 3    

Then type "subl foo.py", it will work. Just add an Environment Variable will work.

###如何在git bash中运行sublime  
[Udacity教程](https://www.udacity.com/wiki/ud775/sublime)
