//本文件为将opacity转换为filter的形式
function setOpacity(){
	if (arguments.length==1) {
		var parm=arguments[0];
	    var result=parm.match(/opacity:(\d?.\d+);/);
	}
	if(result!=null){
		parm=parm.replace(result[0],'filter:alpha(opacity='+parseFloat(result[1])*100+')');
	}
	return parm;
    //return result[1];
}
var a=setOpacity('opacity:0.52;');
var div=document.querySelector('div');
//div.style.filter='alpha(opacity:50)';
//div.style.opacity='0.5'