<?php
if(!defined('ACCESS')) exit;
if(!defined('DEBUG')) define('DEBUG',false);//调试模式
if(!defined('APP_PATH')) define('APP_PATH','./Application/');//应用目录

//编译文件
define('MD_PATH', str_replace('\\', '/', dirname(__FILE__)));
include_once MD_PATH.'/Core/init.class.php';
Boot::run();