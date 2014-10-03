/*HTML5中例子
<div class="detail-tab-area" id="detail-tab-area">
    <!-- 图书描述 -->
    <div class="active">
        <p>《Python基础教程(第2版)》包括Python程序设计的方方面面，首先从Python的安装开始，随后介绍了Python的基础知识和基本概念，包括列表、元组、字符串、字典以及各种语句。然后循序渐进地介绍了一些相对高级的主题，包括抽象、异常、魔法方法、属性、迭代器。此后探讨了如何将Python与数据库、网络、C语言等工具结合使用，从而发挥出Python的强大功能，同时介绍了Python程序测试、打包、发布等知识。最后，作者结合前面讲述的内容，按照实际项目开发的步骤向读者介绍了几个具有实际意义的Python项目的开发过程。</p>
    </div>
    <!-- 基本信息 -->
    <div class="normal">
        <p>出版社: 人民邮电出版社; 第1版 (2010年7月1日)</p>
        <p>外文书名: Beginning Python:From Novice to Professional</p>
        <p>丛书名: 图灵程序设计丛书</p>
        <p>平装: 471页</p>
        <p>语种： 简体中文</p>
        <p>开本: 16</p>
        <p>ISBN: 9787115230270</p>
        <p>条形码: 9787115230270</p>
        <p>商品尺寸: 23.4 x 18.6 x 2.6 cm</p>
        <p>商品重量: 798 g</p>
    </div>
    <!-- 用户评论 -->
    <div class="normal">
        <div class="user">
            <div class="user-image">
            <a href="#"><img src="users.jpg"></a>
            <p>会飞的猪</p>
        </div>
        <div class="user-comment">
            <span>2014-6-7</span>
            <p>这本书不错哦，很适合新手查看。</p>
        </div>
        </div>
        <div class="user">
            <div class="user-image">
            <a href="#"><img src="users.jpg"></a>
            <p>会飞的猪</p>
        </div>
        <div class="user-comment">
            <span>2014-6-7</span>
            <p>这本书不错哦，很适合新手查看。</p>
        </div>
        </div> 
    </div>
</div>
*/
/*在HTML5中调用，依次为父元素及对应的子元素*/
window.onload=function(){
	new Tab("detail-tab-nav",'detail-tab-area',"li","div")
};

/*JS原型链写法*/
function Tab(id,index,btn,content) {
	var _this = this;
	var elem = document.getElementById(id);
	var child = document.getElementById(index)
	this.btn = elem.getElementsByTagName(btn);
	this.con = child.getElementsByTagName(content);
	for (var i = this.btn.length - 1; i >= 0; i--) {
		this.btn[i].index=i;
		this.btn[i].onmousemove=function(){
			_this.fnClick(this); //将this转入，解决this在fnClick中被改变的问题
		}
	};
}

Tab.prototype.fnClick = function(oBtn) {
	for (var i = this.btn.length -1;i >=0;i--){
		this.btn[i].className="normal";
		this.con[i].style.display="none";
	}
	this.btn[oBtn.index].className="active"; //当前按钮索引的class为激活的状态
	this.con[oBtn.index].style.display="block";
};