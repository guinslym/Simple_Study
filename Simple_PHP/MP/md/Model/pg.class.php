<?php
class PG {
	private $link;
	private $host='localhost';
	private $dbname='tim';
	private $user='tim';
	private $password='123456';
	public function __construct(){
		$this->setClientChar();
		$this->connect();
	}

	private function connect(){
		$this->link=pg_connect("host={$this->host} dbname={$this->dbname} user={$this->user} password={$this->password}");
		if(!$this->link){
			echo 'Connection Status: '.$this->getServerStatus();
			echo "<br>Failed to Connect the Postgresql Server";
			echo '<br>无法连接数据库,请检查您的信息配置或与数据库管理人员联系';
			exit;
		}
		
	}

	private function setClientChar(){
		header('content-type:text/html;charset=utf-8');
	}

	public function getFetchAll($sql){
		$query=pg_send_query($this->link, $sql);
		$res=pg_get_result($this->link);
		$fetch=pg_fetch_all($res);
		return $fetch;
	}

	public function getServerStatus(){
		$stat=pg_connection_status($this->link);
		switch ($stat) {
			case 'PGSQL_CONNECTION_OK':
			    $info='当前连接服务器成功';
			    return $info;
				break;
			case '' and 'null':
				$info='当前连接服务器失败';
				return $info;
				break;
			case 'PGSQL_CONNECTION_BAD':
			    $info='当前连接正忙,正在帮你重新连接';
			    return $info;
			    reconnect($this->link);
		}
	}

	public function __destruct(){
		pg_close();
	}
}

$a=new PG();
$sql='select * from cities';
$res=$a->getFetchAll($sql);
var_dump($res);
echo $a->getServerStatus();