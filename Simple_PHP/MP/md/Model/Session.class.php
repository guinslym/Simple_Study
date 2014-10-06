<?php
	//session入库
	class Session extends DB{
		//属性
		protected $table = 'session';

		//构造方法，初始化
		public function __construct(){
			//调用父类的构造方法来连接数据库
			parent::__construct();

			//1.	注册
			session_set_save_handler(
				array($this,'sess_open'),	
				array($this,'sess_close'),	
				array($this,'sess_read'),	
				array($this,'sess_write'),	
				array($this,'sess_destroy'),	
				array($this,'sess_gc')
			);

			//2.	开启session
			@session_start();
		}

		//open方法
		public function sess_open(){
			//获取数据库连接
			//在构造方法中已经使用DB连接了数据库
		}

		//close方法
		public function sess_close(){
			//关闭连接
		}

		//read方法
		public function sess_read($s_id){
			//读取session信息
			$expire = time() - ini_get('session.gc_maxlifetime');
			$sql = "select * from {$this->getTableName()} where s_id = '{$s_id}' and s_expire >= '{$expire}'";

			//执行
			$sess = $this->db_getRow($sql);
			if($sess){
				return $sess['s_info'];
			}

			return '';
		}

		//write方法
		public function sess_write($s_id,$s_info){
			$time = time();
			$sql = "replace into {$this->getTableName()} value('{$s_id}','{$s_info}','{$time}')";

			//执行
			return $this->db_insert($sql);
		}

		//destroy方法
		public function sess_destroy($s_id){
			$sql ="delete from {$this->getTableName()} where s_id = '{$s_id}'";

			//执行
			return $this->db_delete($sql);
		}

		//gc方法
		public function sess_gc($lifetime){
			//回收
			$expire = time() - $lifetime;
			$sql = "delete from {$this->getTableName()} where s_expire < '{$expire}'";

			//执行
			return $this->db_delete($sql);
		}
	}