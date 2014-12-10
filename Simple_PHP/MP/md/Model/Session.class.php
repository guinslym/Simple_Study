<?php
	/*
	session入库类,主要用于解决因为I/0性能导致session读取缓慢
	 */
	class Session extends DB{
		protected $table = 'session';

		public function __construct(){
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

		public function sess_open(){
			mysql_connect();
		}

		public function sess_close(){
			mysql_close();
		}

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

		public function sess_write($s_id,$s_info){
			$time = time();
			$sql = "replace into {$this->getTableName()} value('{$s_id}','{$s_info}','{$time}')";
			return $this->db_insert($sql);
		}

		public function sess_destroy($s_id){
			$sql ="delete from {$this->getTableName()} where s_id = '{$s_id}'";
			return $this->db_delete($sql);
		}

		public function sess_gc($lifetime){
			$expire = time() - $lifetime;
			$sql = "delete from {$this->getTableName()} where s_expire < '{$expire}'";
			return $this->db_delete($sql);
		}
	}