<?php
	/*
	栏目类
	 */
	class Category extends DB{
		public $table = 'category';

		/*
		 * 添加栏目方法
		 * @param1 string $c_name 栏目名
		 * @param2 string $c_keywords 栏目关键字
		 * @param3 string $c_content 栏目内容
		 * @param4 int $c_state 栏目状态 默认1 表示显示
		 * @return boolean 成功返回true 失败返回false
		*/
		public function addCategory($c_name,$c_keywords,$c_content,$c_state){
			$sql = "insert into {$this->getTablename()} (c_name,c_keywords,c_content,c_state) values('{$c_name}','{$c_keywords}','{$c_content}','{$c_state}')";
			$sql=mysql_escape_string($sql);
			return $this->db_insert($sql) ? true : false;
		}

		/*
		 * 获取栏目方法
		 * @param1 int $page 当前页数
		 * @return array() 成功返回栏目信息数组
		*/
		public function getCategory($page = 1){
			//获取每页显示信息条数
			$pagesize = $GLOBALS['config']['pagesize'];
			//获取起始位置
			$start = ($page - 1) * $pagesize;
			$sql = "select * from {$this->getTableName()} where c_is_delete = 1 limit {$start},{$pagesize}";
			$sql=mysql_escape_string($sql);
			return $this->db_getRows($sql);
		}

		/*
		 * 获取总栏目数
		 * @return mixed 成功返回总记录数 失败返回false
		*/

		public function getCounts(){
			$sql = "select count(*) cats from {$this->getTableName()} where c_is_delete = 1";
			$sql=mysql_escape_string($sql);
			$res = $this->db_getRow($sql);
			return $res ? $res['cats'] : false;
		}

		/*
		 * 该变栏目状态
		 * @param1 int $id 需要改变的栏目id
		 * @param2 int $state 当前栏目状态
		 * @return boolean 成功返回true 失败返回false
		*/
		public function changeState($id,$state){
			if($state == 0){
				$state = 1;
			}else{
				$state = 0;	
			}
			$sql = "update {$this->getTableName()} set c_state = {$state} where c_id = {$id}";
			$sql=mysql_escape_string($sql);
			return $this->db_update($sql);
		}

		/*
		 * 编辑栏目状态
		 * @param1 int $id 当前选中的栏目id
		 * @return mixed 成功返回栏目信息数组 失败返回false
		*/
		public function editCategory($id){
			$sql = "select * from {$this->getTableName()} where c_id = {$id}";
			$sql=mysql_escape_string($sql);
			return $this->db_getRow($sql);
		}
		
		/*
		 * 修改栏目方法
		 * @param1 int $id 需要修改栏目的id
		 * @param1 string $c_name 栏目名
		 * @param2 string $c_keywords 栏目关键字
		 * @param3 string $c_content 栏目内容
		 * @return boolean 成功返回true 失败返回false
		*/
		public function updateCategory($c_id,$c_name,$c_keywords,$c_content){
			$sql = "update {$this->getTableName()} set c_name = '{$c_name}',c_keywords = '{$c_keywords}',c_content = '{$c_content}' where c_id = {$c_id}";
			$sql=mysql_escape_string($sql);
			return $this->db_update($sql) ? true : false;
		}

		/*
		 * 删除栏目方法
		 * @param1 int $id 要删除的栏目的id
		 * @return boolean 成功返回true 失败返回false 
		*/
		public function deleteCategory($id){
			$sql = "update {$this->getTableName()} set c_is_delete = 0 where c_id = {$id}";
			$sql=mysql_escape_string($sql);
			return $this->db_update($sql);
		}
        
		/*
		 *返回栏目的名称
		 * @return array 返回栏目名称的数组 
		 */
		public function getCategoryName(){
			$sql="select * from {$this->getTableName()} where c_is_delete = 1";
			$sql=mysql_escape_string($sql);
			return $this->db_getRows($sql);
		}

		public function getCatgoryById($c_id){
			$sql="select * from {$this->getTableName()} where c_id = {$c_id} limit 1";
			$sql=mysql_escape_string($sql);
			return $this->db_getRows($sql);
		}
		
	}
?>