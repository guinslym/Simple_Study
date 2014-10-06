<?php
	//封装一个DB类，用来专门操作数据库，以后凡是对数据的操作都由DB类的对象来实现
	class DB{
		//定义属性
		private $host;
		private $port;
		private $user;
		private $pass;
		private $dbname;
		private $charset;
		private $prefix;		//表前缀
		private $link;			//连接资源

		//构造方法，初始化对象属性
		/*
		 * @param1 array $arr,默认为空，里面是一个关联数组,有7个元素
		 * array('host'=>'localhost','port'=>'3306');
		 */
	 public function __construct($arr = array()){
		//初始化属性 
		$this->host = isset($arr['host']) ? $arr['host'] : $GLOBALS['config']['mysql']['host'];
		$this->port = isset($arr['port']) ? $arr['port'] : $GLOBALS['config']['mysql']['port'];
		$this->user = isset($arr['user']) ? $arr['user'] : $GLOBALS['config']['mysql']['user'];
		$this->pass = isset($arr['pass']) ? $arr['pass'] : $GLOBALS['config']['mysql']['pass'];
		$this->dbname = isset($arr['dbname']) ? $arr['dbname'] : $GLOBALS['config']['mysql']['dbname'];
		$this->charset = isset($arr['charset']) ? $arr['charset'] : $GLOBALS['config']['mysql']['charset'];
		$this->prefix = isset($arr['prefix']) ? $arr['prefix'] : $GLOBALS['config']['mysql']['prefix'];
		//连接数据库
		$this->connect();
		//设置字符集
		$this->setCharset();
		//选择数据库
		$this->setDbname();
	 }
			
	/*
	 * 连接数据库
	 */
	 private function connect(){
		//mysql扩展连接
		$this->link = mysql_connect($this->host.':'.$this->port,$this->user,$this->pass);

		//判断连接
		if(!$this->link){
			//连接出错
			echo '数据库连接失败:<br/>';
			echo '错误编号：'.mysql_errno().'<br/>';
			echo '错误描述：'.mysql_error().'<br/>';
			exit;
		}
	 }

	 /*
	  * 设置字符集
	  */
	  private function setCharset(){
		$this->db_query("set names {$this->charset}");
	  }
	
	/*
	 * 选择数据库
	 */
	 private function setDbname(){
		$this->db_query("use {$this->dbname}");
	 }

	 /*
	  * 增加数据
	  * @param1 string $sql 要执行的插入语句
	  * @return boolean 成功返回自动增长的id 失败返回false 
	  */
	  public function db_insert($sql){
		//发送数据
		$this->db_query($sql);
		//成功返回自增长id
		return mysql_affected_rows() ? mysql_insert_id() : false;
	  }

	  /*
	   * 删除数据
	   * @param1 string $sql 要执行的删除语句
	   * @return boolean 成功返回受影响的行数 失败返回false
	   */
	   public function db_delete($sql){
		//发送sql
		$this->db_query($sql);
		//判断结果
		return mysql_affected_rows() ? mysql_affected_rows() : false;
	   }

	   /*
		* 更新数据
		* @param1 string $sql 要执行的更新语句
		* @return boolean 成功返回收影响的行数 失败返回false
		*/
		public function db_update($sql){
			//执行语句
			$this->db_query($sql);
			//判断结果
			return mysql_affected_rows() ? mysql_affected_rows() : false;
		}

	/*
	 * 查询数据:查询一条记录
	 * @param1 string $sql 要查询的sql语句
	 * @return array() 成功返回一个数组 失败返回空数组
	 */
	 public function db_getRow($sql){
		 //执行语句
		$res = $this->db_query($sql);
		//判断结果
		return mysql_num_rows($res) ? mysql_fetch_assoc($res) : array();
	 }

	 /*
	  * 查询：查询多条记录
	  * @param1 string $sql 要执行的查询语句
	  * @return array() 成功返回一个二维数组 失败返回空数组
	  */
	  public function db_getRows($sql){
		//执行语句
		$res = $this->db_query($sql);
		//判断结果
		$list = array();
		if(mysql_num_rows($res)){
			//遍历结果集存入数组
			while($row = mysql_fetch_assoc($res)){
				$list[] = $row;
			}
		}
		//返回结果
		return $list;
	  }
	  
	  /*
	   * mysql_query错误处理
	   * @param1 string $sql 需要执行的语句
	   * @return mixed 只要语句不出错 全部返回
	  */
	  private function db_query($sql){
		//发送sql
		$res = mysql_query($sql);
		//判断结果
		if(!$res){
			//结果出错了
		echo '语句出现错误:<br/>';
		echo '错误编号：'.mysql_errno().'<br/>';
		echo '错误描述：'.mysql_error().'<br/>';
		exit;
		}
		return $res;
	   }

	   //设置自动添加前缀名
	   protected function getTableName(){
		return $this->prefix.$this->table;
	   }

	   //DB类被序列化时需要保存的数据
	   public function __sleep(){
		return array('host','port','user','pass','dbname','charset','prefix');
	   }
		//DB类被反序列化是 需要加载的操作
	   public function __wakeup(){
			//连接数据库
			$this->connect();
			//设置字符集
			$this->setCharset();
			//选择数据库
			$this->setDbname();
		}
	}

?>