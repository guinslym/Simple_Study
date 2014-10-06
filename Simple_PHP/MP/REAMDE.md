##介绍##
本框架自带Smarty和Ueditor，是1个单一入口的轻量级框架。  
作者:猪猪侠

##使用方法##
在根目录下新建1个文件，例如index.php，然后类似如下形式书写其内容即可。  
其中:

- DEBUG表示开启调试模式
- APP_PATH表示应用的根路径
 
```
<?php
define('ACCESS','ACC');
define('DEBUG',true);
define('APP_PATH','Home/');
define('PATH',str_replace('\\','/',dirname(__FILE__)));

//引入初始化文件
include PATH.'/md/init.php';
```
