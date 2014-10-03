function M(arg){
	return new VQuery(arg);
}

function addEvent (obj,ev,fn) {
	if (obj.attachEvent) {
		obj.attachEvent('on'+ev,function(){
			fn.call(obj);//用于解决IE9以下版本传入this时this为window而不是当前对象。call()中传入的参数是什么，this就是什么。
		});
	}else{
		obj.addEventListener(ev,fn,false);
	}
}

function getStyle(obj,attr){
	if (obj.currenStyle) {
		return obj.currenStyle[attr];
	}else{
		return getComputedStyle(obj,null)[attr];
	}
}

function getByClass(parent,mclass){
	var elem=parent.getElementsByTagName('*'),
	result=[],
	i=0;
    for (var i = elem.length - 1; i >= 0; i--) {
    	if (elem[i].className==mclass) {
    		result.push(elem[i]);
    	}
    }
    return result;
}

function appendArr(arr1,arr2){
	for (var i = arr2.length - 1; i >= 0; i--) {
		arr1.push(arr2[i]);
	};
}

function getIndex(obj){
	var Bro=obj.parentNode.children;
	for (var i = Bro.length - 1; i >= 0; i--) {
		if(Bro[i]==obj){
			return i;
		}
	}
}

function VQuery (arg) {
	this.element=[];
	switch(typeof arg){
		case 'function':
		addEvent(window,'load',arg);
		break;
		case 'string':
			switch(arg.charAt(0)){
				case '#':
				   var obj=document.getElementById(arg.substring(1));
                   this.element.push(obj);
				   break;
				case '.':
                    this.element=getByClass(document,arg.substring(1));
				    break;
				default:
				    this.element=document.getElementsByTagName(arg);
			}
		break;
		case 'object':
		this.element.push(arg);
	}
}
VQuery.prototype.on=function(type,fn){
	var i=0;
	for (var i = this.element.length - 1; i >= 0; i--) {
		addEvent(this.element[i],type,fn);
	};
};

VQuery.prototype.css=function(attr,value){
	if (arguments.length==2) {
		var i=0;
		for (var i = this.element.length - 1; i >= 0; i--) {
			this.element[i].style[attr]=value;
		}
	}else{
		return getStyle(this.element[0],attr);
	}
}

VQuery.prototype.eq=function(n){
	return M(this.element[n]);
};

VQuery.prototype.find=function(str){
	var i=0,result=[];
	for (var i = this.element.length - 1; i >= 0; i--) {
		switch(str.charAt(0)){
			case '.':
			    var elem=getByClass(this.element[i],str.substring(1));
			    result=result.concat(elem);
				break;
			default:
			    var elem=this.element[i].getElementsByTagName(str);
			    appendArr(result,elem);
		}
	}
	var _jQuery=M();
	_jQuery.element=result;
	return _jQuery;
}

VQuery.prototype.index=function(){
	return getIndex(this.element[0]);
};

VQuery.prototype.attr=function(attr,value){
	if (arguments.length==2) {
		for (var i = this.element.length - 1; i >= 0; i--) {
			this.element[i][attr]=value;
		};
	}else{
		return this.element[0][attr];
	}
};