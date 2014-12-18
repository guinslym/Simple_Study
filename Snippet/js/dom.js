/*
 *本js脚本为dom操作所用,使用字符串提取第1个字符来判断传入参数的类型
 *如果字符串为'#xxx'类型,则使用document.getElementById()来创建1个元素对象
 */
function dom(elem,parent){
	if (parent===undefined) {
		parent=document;
	};
	if(!document.querySelector){
		if (elem.indexOf('#')>-1) {
			elem=elem.slice(1);
			return parent.getElementById(elem);
	    }
	}else{
		return parent.querySelector(elem);
	}
}