<head>
  <title>This is my diary website.</title>
  <meta charset = "utf-8">
</head>

<body>

<h2>Hey dude, anything wanna share today? </h2>
<p>Just <b>feel free</b> to tell me!</p>
<pre><p>日记就像岩钉，
不但记录你成长的过程，
还防止你被摔死！
Lol.</p></pre>

<form action="/diary" method="post">
Write diary here:<br>
	<input type="text" style="width:300px; height:35px" name="typein"/>
	<input type="submit" value="Submit"/>
</form>

<p>以下是往期日记：<hr>
<pre>
<textarea rows="40" cols="120">{{content}}</textarea>
</pre>
</p>

</body>