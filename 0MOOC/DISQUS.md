# DISQUS 私人教程

## 背景
在Gitbook只能单方面输出，无法交流，为了和小伙伴一起愉快的沟通，需要在页面上插入Disqus评论插件，这是刚性需求，嗯，就是这样的。

## 配置
###要搞定两点
####1.Disqus注册
不注册Disqus，你评论数据如何保存，所以这是第一步。

账号注册完以后在右上角有一个齿轮的标记 setting，在下拉列表中选择 add disqus to site，需要填写 Site name (应该就是你的shortname，book.json里的核心变量，让disqus找到你)，Site URL(shortname.disqus.com)，完事后就注册了一个账号(可以注册多个)。
然后
- 选择 setting
- 选择 advanced
- 在下面的Trusted Domains中，添加 gitbook.com， gitbooks.io   （一行一条网址，不用加www）

####2.配置book.json文件
新建book.json文件，内容如下：
```
{
    "plugins": ["disqus"],
    "pluginsConfig": {
        "disqus": {
            "shortName": "改成你在disqus上的shortname"
        }
    }  
}
```
如果和github的仓库联动的话，把这个文件放在仓库根目录下就万事大吉了，是也乎。不联动的情况没有折腾，应该放在Files Tree里就行，无暇考证。

## 体验
别人的回复可以收到邮件提醒，多贴心，不用刷，哈哈。
配置成功的时候，心情可以用**"是也乎"**来表达。
