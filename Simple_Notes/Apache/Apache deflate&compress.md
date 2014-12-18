Apache压缩处理.md
首先,客户端浏览器需要告诉服务器支持哪些压缩格式,有助于更好的让服务器提供合适的资源给客户端。我们可以在浏览器的请求头信息的Accept-Encoding可以看出浏览器支持的压缩格式。

##配置步骤##

1. 在apache的apache.conf中加载deflate模块`/etc/apache2/moda_available/deflate.conf`。
2. 在虚拟主机中进行配置。

```
<Directory "/var/www/html">
...
<IfModule mod_deflate.c>
	<IfModule mod_filter.c>
		# these are known to be safe with MSIE 6
		AddOutputFilterByType DEFLATE text/html text/plain text/xml

		# everything else may cause problems with MSIE 6
		AddOutputFilterByType DEFLATE text/css            #压缩css文件
		AddOutputFilterByType DEFLATE application/x-javascript application/javascript application/ecmascript
		AddOutputFilterByType DEFLATE application/rss+xml
		AddOutputFilterByType DEFLATE application/xml
	</IfModule>
</IfModule>
</Directory>
```
