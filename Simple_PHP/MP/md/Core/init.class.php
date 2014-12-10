<?php

//初始化类
class Boot{
	public static function run(){
	self::setHeader();
	self::setConst();
	self::setErrors();
  self::mkDir();
	self::setSession();
	self::loadConfig();
  self::setAutoload();
	self::setUrl();
	self::setDispatch();
	}

	//1. 初始化字符集
	private static function setHeader(){
	    header('content-type:text/html;charset=utf-8');
	}

	//2. 定义系统目录
	private static function setConst(){
		$root=dirname($_SERVER['SCRIPT_FILENAME']);
		define('ROOT', $root."/md/");
		define('CORE', ROOT."Core/");//框架核心目录
		define('MODEL', ROOT."Model/");//框架模型目录
		define('ACTION',ROOT."Action/");//框架控制器目录
		define('VIEW', ROOT.'View/');//框架视图目录
		define('CONF', ROOT."Conf/");//框架配置目录
		define('ROOT_PUB',ROOT.'Public/');//框架公共目录
		define('APP_MODEL', APP_PATH.'Model/');//应用模型目录
		define('APP_ACTION',APP_PATH.'Action/');//应用控制器目录
		define('APP_VIEW', APP_PATH.'View/');//应用视图模板目录
		define('APP_CORE',APP_PATH.'Core/');//应用核心类目录
		define('APP_CONF',APP_PATH.'Conf/');//应用配置文件目录
		define('APP_PUB',APP_VIEW.'Public/');//应用视图公共文件目录
        define('SMARTY',ROOT_PUB.'Smarty/');//Smarty引擎的文件目录
        define('UEDITOR',ROOT_PUB.'Ueditor/');//百度编辑器的文件目录
	}

	//设置错误模式
	private static function setErrors(){
	    @ini_set('error_reporting', 1);
	    @ini_set('display_errors', 1);
	}


	//自动加载核心文件
	public static function loadCoreFile($class){
		if(is_file(APP_CORE."$class.class.php")){
			include_once APP_CORE."$class.class.php";
		}
	}

	//自动加载配置文件
	public static function loadConfig(){
		$GLOBALS['config']=include_once APP_CONF.'/config.php';
	}

	//自动加载模型类
	public static function loadModel($class){
		if (is_file(APP_MODEL."$class.class.php")) {
			include_once APP_MODEL."$class.class.php";
		}
	}
    //加载Smarty配置文件
    public static function loadSmarty($class){
        if(is_file(SMARTY."$class.class.php")){
            include_once SMARTY."$class.class.php";
        }
    }

  //自动加载控制器类
	public static function loadAction($class){
	    if (is_file(APP_ACTION."$class.class.php")) {
		    include_once APP_ACTION."$class.class.php";
	    }
	}

	//开启Session
	private static function setSession(){
		@session_start();
	}

	//开启自动加载机制
	private static function setAutoload(){
		spl_autoload_register(array('Boot','loadCoreFile'));
    spl_autoload_register(array('Boot','loadSmarty'));
		spl_autoload_register(array('Boot','loadModel'));
    spl_autoload_register(array('Boot','loadAction'));
	}

	//设置URL截取模式
	private static function setUrl(){
		$module=isset($_REQUEST['m'])? $_REQUEST['m'] : 'index';
		$action=isset($_REQUEST['c'])? $_REQUEST['c'] : 'index';

		$module=strtolower($module);
		$action=strtolower($action);

		$module=ucfirst($module);

		define('MODULE', $module);
		define('ACT', $action);
	}

	//创建应用目录
	private static function mkDir(){
		if (is_dir(APP_PATH)) return;
		$dirs=array(
			APP_CORE,
			APP_ACTION,
			APP_VIEW,
			APP_MODEL,
			APP_CONF
		);
		foreach ($dirs as $d) {
			if (!is_dir($d)) {
				$dir=mkdir($d,0757,true);//利用递归解决文件夹创建失败的问题
				if (!$dir) {
					header('content-type:text/html;charset=utf-8');
					exit("目录{$d}创建失败,请检查权限");
				}else{
					copy(CORE."View.class.php",APP_CORE."View.class.php");
					copy(CORE."Action.class.php",APP_CORE."Action.class.php");
					copy(MODEL."DB.class.php",APP_MODEL."DB.class.php");
					copy(CONF."config.php",APP_CONF."config.php");
				    copy(ACTION."IndexAction.class.php",APP_ACTION."IndexAction.class.php");
				}
			}
	    }
	}

	//设置分化应用
	private static function setDispatch(){
		$module= MODULE.'Action';
		$module = new $module();
		$action= ACT;
		$module->$action();
	}
}
