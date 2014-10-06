<?php
	class Captcha{
		//定义属性
		private $width;				//验证码图片宽度
		private $height;				//验证码图片高度
		private $length;				//验证码长度
		private $lines;				//干扰线数量
		private $pixels;				//干扰点属性
		private $color;				//各种字体颜色
		private $font;				//字体大小
		private $string;				//目标字符串

		//构造方法
		public function __construct($arr = array()){
			$this->width = isset($arr['width']) ? $arr['width'] : 80;
			$this->height = isset($arr['height']) ? $arr['height'] : 25;
			$this->length = isset($arr['length']) ? $arr['length'] : 4;
			$this->lines = isset($arr['lines']) ? $arr['lines'] : 5;
			$this->pixels = isset($arr['pixels']) ? $arr['pixels'] : 500;
			$this->font = isset($arr['font']) ? $arr['font'] : 5;
			$this->color['bg_min'] = isset($arr['bg_min']) ? $arr['bg_min'] : 200;
			$this->color['bg_max'] = isset($arr['bg_max']) ? $arr['bg_max'] : 255;
			$this->color['font_min'] = isset($arr['font_min']) ? $arr['font_min'] : 0;
			$this->color['font_max'] = isset($arr['font_max']) ? $arr['font_max'] : 100;
			$this->color['line_min'] = isset($arr['line_min']) ? $arr['line_min'] : 100;
			$this->color['line_max'] = isset($arr['line_max']) ? $arr['line_max'] : 150;
			$this->color['pixe_min'] = isset($arr['pixe_min']) ? $arr['pixe_min'] : 150;
			$this->color['pixe_max'] = isset($arr['pixe_max']) ? $arr['pixe_max'] : 200;

			$this->string=isset($arr['string']) ? $arr['string'] : 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789';
		}

		//获得验证图片
		public function getYZ(){
			//创建画布
			$im = imagecreatetruecolor($this->width,$this->height);

			//随机背景颜色
			$bg_color = imagecolorallocate($im,mt_rand($this->color['bg_min'],$this->color['bg_max']),mt_rand($this->color['bg_min'],$this->color['bg_max']),mt_rand($this->color['bg_min'],$this->color['bg_max']));
			//填充背景色
			imagefill($im,0,0,$bg_color);

			//增加干扰线
			for($i=0;$i<$this->lines;$i++){
				//随机干扰线的颜色
				$line_color=imagecolorallocate($im,mt_rand($this->color['line_min'],$this->color['line_max']),mt_rand($this->color['line_min'],$this->color['line_max']),mt_rand($this->color['line_min'],$this->color['line_max']));

				//写入
				imageline($im,mt_rand(0,$this->width),mt_rand(0,$this->height),mt_rand(0,$this->width),mt_rand(0,$this->height),$line_color);
			}

			//增加干扰点
			for($i=0;$i<$this->pixels;$i++){
				//获取随机干扰点颜色
				$pixel_color=imagecolorallocate($im,mt_rand($this->color['pixe_min'],$this->color['pixe_max']),mt_rand($this->color['pixe_min'],$this->color['pixe_max']),mt_rand($this->color['pixe_min'],$this->color['pixe_max']));

				//写入
				imagesetpixel($im,mt_rand(0,$this->width),mt_rand(0,$this->height),$pixel_color);
			}

			//获取验证码
			$captcha = $this->getCaptchaString();

			//给验证码分配随机颜色
			$str_color = imagecolorallocate($im,mt_rand($this->color['font_min'],$this->color['font_max']),mt_rand($this->color['font_min'],$this->color['font_max']),mt_rand($this->color['font_min'],$this->color['font_max']));

			//将验证码写入图片
			imagestring($im,$this->font,ceil($this->width/2)-17,ceil($this->height/2)-10,$captcha,$str_color);



			//获取图片
			imagepng($im);

			//释放资源
			imagedestroy($im);

		}

		//获取验证码
			private function getCaptchaString(){
				$captcha = '';
				for($i=0;$i<$this->length;$i++){
					$captcha .= $this->string[mt_rand(0,strlen($this->string) - 1)];
				}
				//将生成的验证码写入session中
				$_SESSION['captcha']=$captcha;
				return $captcha;
			}


		//验证验证码
		public static function checkCaptcha($captcha){
			//验证码不区分大小写，所以将需要比对的验证码和用户输入的验证码全部转换成为大写
			return (strtoupper($captcha) === strtoupper($_SESSION['captcha']));
		}
	}