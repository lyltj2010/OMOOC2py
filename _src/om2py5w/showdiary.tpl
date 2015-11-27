<head>
  <title>This is my diary website.</title>
  <meta charset = "utf-8">
  <style>
  #header {
    background-color: black;
    color: white;
    text-align: center;
    padding:5px;
  }
  #nav {
    line-height: 30px;
    font-size: 120%;
    background-color: #eeeeee;
    height: 450px;
    width: 20%;
    float: left;
    padding: 5px;
  }
  #section {
    width: 75%;
    float: left;
    padding:10px;
  }
  #footer {
    background-color: black;
    color: white;
    clear: both;
    text-align: center;
    padding: 5px;
  }
  </style>
</head>
<body>

<div id="header">
<h1>盲人摸象</h1><br>
We first raise the dust and then claim we cannot see.
</div>

<div id="nav">
<pre><p>日记就像岩钉，
不但记录你成长的过程，
还防止你被摔死！
Lol.</p></pre>
</div>

<div id="section">
<form action="/" method="post">
Diary&nbsp<input type="text" style="width:350px;" name="typein"/>&nbsp
Tag&nbsp<input type="text" style="width:100px" name="tag"/>&nbsp
<input type="submit" value="Submit"/>
</form>
<p style="font-family:courier; text-align:center">记录时间的脚印<br>
<pre>
<textarea rows="25" readonly="readonly" style="font-size:120%;text-align:center; width:100%">{{content}}</textarea>
</pre>
</p>
</div>

<div id="footer">
<a href="https://github.com/lyltj2010?tab=repositories" target="_blank">Github</a>&nbsp
<a href="https://www.gitbook.com/@yongle/dashboard" target="_blank">Gitbook</a>
</div>


</body>