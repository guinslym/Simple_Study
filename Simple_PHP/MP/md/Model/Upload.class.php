<?php
	class Upload{
		public static $errorInfo;
		public static $multiErrorInfo;

		public static function uploadSingle($file,$allow,$max	){
			//判断文件类型是否合理
			if(!is_array($file)){
				self::$errorInfo = "当前不是一个合法文件信息！";
				return false;
			}
			//判断文件类型是否合法
			if(!in_array($file['type'],$allow)){
				self::$errorInfo = "当前文件不允许上传！可以上传的类型有：" . implode(',',$allow);
				return false;
			}
			//处理文件错误代码
			switch($file['error']){
				case 1:
					self::$errorInfo='文件过大！已经超过服务器允许大小！';
					return false;
				case 2:
					self::$errorInfo='文件过大！已经超过浏览器允许大小！';
					return false;
				case 3:
					self::$errorInfo='文件上传不完整！';
					return false;
				case 4:
					self::$errorInfo='没有选择要上传的文件！';
					return false;
				case 6:
					self::$errorInfo='找不到服务器文件的临时目录！';
					return false;
				case 7:
					self::$errorInfo='没有权限将文件上传到目标文件夹！';
					return false;
				case 0:
					//判断文件大小是否在自定义允许范围中
					if($file['size'] > $max){
						self::$errorInfo = '文件大小，当前商品只允许上传' . $max . '字节大小！';
						return false;
					}
			}

			//处理文件
			//获取新的文件名字
			$newname = self::getNewName($file['name']);
			if(move_uploaded_file($file['tmp_name'],ADMIN_UPL . '/' . $newname)){
				return './uploads/' . $newname;
			}else{
				self::$errorInfo = '文件移动失败！';
				return false;
			}
			
		}

		private static function getNewName($filename){
			//获取文件的后缀名
			$extension = substr($filename,strrpos($filename,'.'));
			
			//生成新名字
			$newname = date('YmdHis');

			//拼凑随机字符串
			$str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
			for($i=0;$i<5;$i++){
				$newname .= $str[mt_rand(0,strlen($str) - 1)];
			}
			
			//返回随机名字
			return $newname.$extension;
		}

		/*
		 * 多文件上传
		 * @param1 array , 多维数组
		*/
		public static function uploadMultiple($file){
			//定义一个数组保存上传路径
			$upload_arr = array();

			//遍历数组
			foreach($file as $single){
				//判断$single下的name属性是否是一个数组，如果是一个数组，表示文件在上传的时候是采用数组的形式上传，否则是采用单个文件名上传
				if(is_array($single['name'])){
					//多文件遍历
					for($i=0,$length=count($single['name']);$i<$length;$i++){
						//构建文件数组
						$arr = array(
							'name' => $single['name'][$i],
							'type_name' => $single['type_name'][$i],
							'type' => $single['type'][$i],
							'error' => $single['error'][$i],	
							'size' => $single['size'][$i]
						);

						//得到单独文件
						if($path = self::uploadSingle($arr)){
							$upload_arr[$i] = $path;
						}else{
							self::$multiErrorInfo[$i] = self::$errorInfo;
						}
					}
				}else{
					//单文件
					if($path = self::uploadSingle($single)){
						$upload_arr[$i] = $path;
					}else{
						self::$multiErrorInfo[$i] = self::$errorInfo;
					}
				}
			}

			return $upload_arr;
		}
	}