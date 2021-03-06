<?php
	/*
	图片处理类,可以用于创建略缩图和水印
	 */
	class Image{
		private $thumb_width;                                //缩略图的宽度
		private $thumb_height;                               //缩略图的高度
		public $errorinfo;                                   //上传过程中可能出现的错误
		private $image_type = array(                         //允许上传的图片类型
			'gif' => 'gif',
			'png' => 'png',
			'jpg' => 'jpeg',
			'jpeg' => 'jpeg'
		);

		public function __construct($width='',$height=''){
			$this->thumb_width = empty($width) ? $GLOBALS['config']['goods_img_thumb_width'] : $width;
			$this->thumb_height = empty($height) ? $GLOBALS['config']['goods_img_thumb_height'] : $height;
		}

		/*
		 * 根据图片制作缩略图
		 * @paran1 string $file，缩略图原图资源
		 * @return mixed，成功返回缩略图路径，失败返回FALSE
		*/
		public function createThumb($file){
			if(!is_file($file)){
				$this->errorinfo = '不是一个有效的图片！';
				return false;
			}

		//判断文件类型和获取文件的后缀名
		//strrpos获取后面参数最后出现的位置
		$extension = substr($file,strrpos($file,'.')+1);
		
		if(!array_key_exists($extension,$this->image_type)){
			$this->errorinfo = '不是一个有效的图片！';
			return false;
		}
			//创建给定类型的画布
			$imagecreate ='imagecreatefrom' . $this->image_type[$extension];
			//保存的图片类型
			$imagesave = 'image' . $this->image_type[$extension];
			
			$src = $imagecreate($file);

			//创建缩略图资源
			$dst = imagecreatetruecolor($this->thumb_width,$this->thumb_height);

			//获取图片信息
			//getimagesize 获取图片的大小
			$fileinfo = getimagesize($file);
			
			//2. 采样和复制
			if(imagecopyresampled($dst,$src,0,0,0,0,$this->thumb_width,$this->thumb_height,$fileinfo['0'],$fileinfo['1'])){
				$name = 'thumb_' . basename($file);

				if($imagesave($dst,ADMIN_UPL . '/' . $name)){
					return './upload/' . $name;
				}else{
						$this->errorinfo = '缩略图保存失败！';
						return false;
					}
			}else{
				$this->errorinfo = '缩略图采样失败！';
				return false;
			}
		}

			/*
		 * 制作水印
		 * @param1 string $file，要创建水印的图片
		 * @param2 string $position，水印图的位置，默认是0,表示右下角
		 * @param3 int $pct，透明度，默认为30
		 * @param4 string $water，水印的图片，可以使用默认值
		 * @return   string $path，水印图的路径
		*/
		public function createWatermark($file,$position = 0,$pct = 30,$water = ''){
			//判断目标文件是否正确

			if(!$extension = $this->checkFile($file)) return false;

			//判断水印图片是否存在
			if(!$water){
				//使用默认的水印图
				$water = $GLOBALS['config']['goods_img_water'];
			}
			//var_dump($water);exit;
			if(!$water_ext = $this->checkFile($water)){
				$this->errorinfo = '水印图片资源不存在';
				return false;
			}

			//1.		获取图片资源
			$dstcreate = 'imagecreatefrom' . $this->image_type[$extension];
			$watercreate = 'imagecreatefrom' . $this->image_type[$water_ext];
			$dstsave = 'image' . $this->image_type[$extension];

			//2.		获取图片资源
			$dst = $dstcreate($file);
			$wat = $watercreate($water);

			//3.		获取图片信息
			$dstinfo = getimagesize($file);
			$watinfo = getimagesize($water);

			//4.		计算水印在原图的位置
			switch($position){
				case 1:
					//左上角
					$start_x = 0;
					$start_y = 0;
					break;
				case 2:
					//右上角
					$start_x = $dstinfo[0] - $watinfo[0];
					$start_y = 0;
					break;
				case 3:
					//中间位置
					$start_x = floor(($dstinfo[0] - $watinfo[0]) / 2);
					$start_y = floor(($dstinfo[1] - $watinfo[1]) / 2);
				case 4:
					$start_x = 0;
					$start_y = $dstinfo[1] - $watinfo[1];
				case 5:
					default:
					$start_x = $dstinfo[0] - $watinfo[0];
					$start_y = $dstinfo[1] - $watinfo[1];
			}

			//5.		采样合并
			if(imagecopymerge($dst,$wat,$start_x,$start_y,0,0,$watinfo[0],$watinfo[1],$pct)){
				$name = 'water_' . basename($file);
				if($dstsave($dst,ADMIN_UPL . '/' . $name)){
					imagedestroy($dst);
					imagedestroy($wat);
					return './uploads/' . $name;
				}else{
					$this->errorinfo = '水印图片保存失败！';
				}
			}else{
				$this->errorinfo = '水印图片合并失败！';

			}
			imagedestroy($dst);
			imagedestroy($wat);
			return false;
		}

		/*
		 * 判断文件是否有效
		 * @param1 string $file 需要判断的文件
		*/
		private function checkFile($file){
			if(!is_file($file)){
				//不是文件
				$this->errorinfo = '不是一个有效的文件！';
				return FALSE;
			}

			//判断文件类型
			//获取文件的后缀名
			$extension = substr($file,strrpos($file,'.')+1); //不要点

			//判断
			if(!array_key_exists($extension,$this->image_type)){
				//不是一张合法的图片
				$this->errorinfo = '不是一个有效的图片！';
				return false;
			}
			return $extension;
		}
	}