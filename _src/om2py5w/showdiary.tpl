<head>
  <title>This is my diary website.</title>
  <meta charset = "utf-8">
</head>

<body style="background-color:lightgrey">

<h1 style="text-align:center">Hey dude, anything wanna share today? 
</h1>

<p style="font-family:courier;font-size:120%">
Just <b>FEEL FREE</b> to tell me!
</p>

<pre><p style="font-family:courier;font-size:120%">日记就像岩钉，
不但记录你成长的过程，
还防止你被摔死！
Lol.</p></pre>

<form action="/" method="post">
Diary:
	<input type="text" style="width:300px;font-family:courier;background-color:lightgrey;font-family:courier" name="typein"/>
Tag:
	<input type="text" style="width:80px;font-family:courier;background-color:lightgrey;font-family:courier" name="tag"/>
	<input type="submit" value="Submit" style="background-color:lightgrey" />
</form>

<p style="font-family:courier">以下是以往日志：<hr>
<pre>
<textarea rows="40" readonly="readonly" style="font-family:courier;font-size:150%;text-align:center;background-color:lightgrey;width:100%">
{{content}}
</textarea>
</pre>
</p>

</body>