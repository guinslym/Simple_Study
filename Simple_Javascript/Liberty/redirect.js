var parm={};
function redirect (parm) {
	this.t=parm.time;
	this.href=parm.href;
	this.h=document.getElementsByTagName('h1')[0];
	setInterval(function(){
		if (this.t<=0) {
		window.location.href=this.href;
	    };
		this.h.innerHTML="页面将于"+t+"秒后跳转到首页。";
		this.t--;
	},1000);
}

var parms={
	'time':4,
	'href':"http://localhost/shop/admin/privilege.php",
};
redirect(parms);