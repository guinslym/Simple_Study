<?php

/*
验证码类,可以选择2种类型，普通型和标准型
 */
class Code
{
    private $width; //验证码宽度
    private $height; //验证码高度
    private $length; //验证码长度
    private $lines; //干扰线数量
    private $pixels; //干扰点数量
    private $fonts; //字体大小
    private $string; //目标字符串
    private $im;     //验证码实例化对象
    private $type;   //选择验证码的类型

    /*
     *创建构造方法
     */
    public function __construct($arr = array())
    {
        $this->width = isset($arr['width']) ? $arr['width'] : 146;
        $this->height = isset($arr['height']) ? $arr['height'] : 36;
        $this->length = isset($arr['length']) ? $arr['length'] : 4;
        $this->lines = isset($arr['lines']) ? $arr['lines'] : 5;
        $this->pixels = isset($arr['pixels']) ? $arr['pixels'] : 200;
        $this->fonts = isset($arr['fonts']) ? $arr['fonts'] : 24;
        $this->string = isset($arr['string']) ? $arr['string'] : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $this->type=isset($arr['type'])?(int)$arr['type']:0;
    }

    /*
     *获取验证码图片
     */
    public function generate()
    {
        //创建画布
        $this->im = imagecreatetruecolor($this->width, $this->height);
        $bgColor = imagecolorallocate($this->im, mt_rand(200, 255), mt_rand(127, 255), mt_rand(0, 127));
        imagefill($this->im, 0, 0, $bgColor);

        //获取验证码
        $string = $this->getString();

        //分配字符串颜色
        $str_color = imagecolorallocate($this->im, mt_rand(0, 127), mt_rand(0, 127), mt_rand(0, 127));
        //将文字写入到图片，需要注意的是字体必须是开源字体才能在Linux下运行
        switch($this->type){
            case 1:
                imagettftext($this->im, $this->fonts, -3, mt_rand(10, imagesx($this->im) /2), mt_rand(imagesy($this->im)/2,imagesy($this->im)),$str_color, './FreeMono.ttf', $string);
                break;
            case 0:
                imagestring($this->im, $this->fonts, mt_rand(imagesx($this->im)/5,imagesx($this->im)/2), mt_rand(imagesy($this->im)/5,imagesy($this->im)/3), $string, $str_color);
                break;
        }

        //增加干扰线
        $this->getLine();

        //增加干扰点
        $this->getPixel();

        //保存输出
        header('content-type:image/png');
        imagepng($this->im);

        //释放资源
        imagedestroy($this->im);
    }

    private function getString()
    {
        $str = "";
        for ($i = 0; $i < $this->length; $i++) {
            $str .= $this->string[mt_rand(0, strlen($this->string) - 1)];
        }
        $_SESSION['captcha']=$str;
        return $str;
    }

    private function getLine()
    {
        for ($i = 0; $i < $this->lines; $i++) {
            $line_color = imagecolorallocate($this->im, mt_rand(127, 255), mt_rand(0, 127), mt_rand(0, 127));
            imageline($this->im, mt_rand(-10, imagesx($this->im)), mt_rand(-10, imagesy($this->im)), mt_rand(0, imagesx($this->im)), mt_rand(0, imagesy($this->im)), $line_color);
        }
    }

    private function getPixel()
    {
        for ($i = 0; $i < 500; $i += 2) {
            $color = imagecolorallocate($this->im, mt_rand(0, 127), mt_rand(0, 127), mt_rand(0, 127));
            imagesetpixel($this->im, mt_rand(0, imagesx($this->im)), mt_rand(0, imagesy($this->im)), $color);
        }
    }

    /*
     *验证用户提交的验证码
     */
    public static function checkCode($str){
    return strtolower($str) === strtolower($_SESSION['captcha']);
    }
}
