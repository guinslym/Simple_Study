<?php

class View extends Smarty{
  public function __construct(){
    Parent::__construct();
    $this->setTemplateDir(APP_VIEW.MODULE);           //设置模板的路径
    $this->cacheing=false;
  }
}
