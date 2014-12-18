Apache缓存设置.md
##进行缓存处理##
在虚拟主机配置中,添加字段expiresactive和expiresbytype。

```
ServerName www.example.com
<Directory "/var/www/html">
   expiresactive on                                    #开启缓存配置
   expiresbytype image/jpeg "access plus 10 days"      #缓存的类型为image/jpeg,添加10天
   ...
</Directory>
```

##部分文件不缓存处理##

###header设置###
开启Apache配置文件中的header模块`/etc/apache2/mods-available/headers.load
`,在虚拟主机中进行如下配置:

```
ServerName www.example.com
<Directory "/var/www/html">
   expiresactive on                                    #开启缓存配置
   expiresbytype image/jpeg "access plus 10 days"      #缓存的类型为image/jpeg,添加10天
   <filesmatch "\.(gif)$">                             ##匹配以gif后缀的文件
   header set cache-control "no-store,must-revalidate" #设置缓冲控制,不缓存,必须再次验证
   </filesmatch>
   ...
</Directory>
```

重启Apache后,浏览器中对应gif文件不再缓存,从304变为200.
