if (typeof(M)=="undefined") {
	M={};
	M.name='M';
	M.VERSION=0.1;
}

//创建构造器函数，所有函数以此作为模型，对其进行继承
M.class=function(klass,prototype){
	//如果传入的包含initialize属性，则c为klass.initialize
	if (klass&&klass.initialize) {
		var c=klass.initialize;
	}else if(klass&&klass.base){
		var c=function(){
			return klass.base[0].apply(this,arguments); //将所有的参数都传递给klass.base[0]
		}
	}else{
		var c=function(){};//如果上述2种情况，在本js中都没有定义，返回1个空的函数
	}
	c.prototype=prototype||{};
	c.prototype.constructor=c;//继承于c变量，利用c作为原型的构造函数
	M.class.inherit(c,klass);
	if (klass&&klass.base) {
		for(var i=0,len=klass.base.length;i<len;i++){
			var parent=klass.base[i];
			if (i==0) {
				c.SUPER=parent;
				c.prototype.SUPER=parent.prototype;//创建超类属性或方法
			}
			M.class.inherit(c,parent);
			M.class.inherit(c.prototype,parent.prototype);
		}
	}
	return c;
};

M.class.inherit=function(child,parent){
	for(var prop in parent){
		if (typeof(child[prop])!='undefined'||prop=='initialize') continue;//对于子类没有的属性，退出循环后再次进入
		child[prop]=parent[prop];//利用原型链引用，获得父类的所有属性
	}
}

//DOM方法，用于获取节点
M.DOM=new M.class({
	g:function(id){
		if (!id) {return null};
		if (typeof id=="string"||id instanceof String) {
			return document.querySelector(id);
		}else if(id.nodeName&&(id.nodeType==1||id.nodeType==9)){
			//如果获取到的是对象，可以得到其元素标签名和(元素或document节点直接返回)
			return id;
		}
		return null;
	}
	,
	getByClassName:function(className,parent){
		if (typeof parent=="undefined") {
			parent=document;
		}
		var ret=[];
		//如果原生支持getElementsByClassName
		if (parent.getElementsByClassName) {
			var nodes = parent.getElementsByClassName(className);
			for(var i=0,len=nodes.length;i<len;i++){
				ret.push(nodes.item(i));
			}
			return ret;
		}else{
			var elems=parent.childNodes;
			for (var i = 0,len=elems.length; i < len; i++) {
				if (elems[i].className==className) {
					ret.push(elems[i]);
				}
			}
			return ret;
		}
	},
	
	//传入1个对象及其class,主要是利用字符串的indexOf查找其位置，最小为0，找不到为-1
	hasClassName:function(element,className){
		//如果参数没有传入，直接返回
		if (!element||!className) {return false};
		var cname=element.className;
		//如果该元素没有类名，直接返回
		if (!cname) {return false};
		cname=''+cname.toLowerCase()+'';
		cname=cname.replace(/[\n\r\t]/g,'');
		className=''+className.toLowerCase()+'';
		return (cname.indexOf(className)>-1);
	},
	addClassName:function(element,className){
		if (M.DOM.hasClassName(element,className)) {return};
		var c=element.className||''; //对象原有的class
		//如果元素的class长度大于0，返回叠加后的，否则是传入的类型，因为JS隐式转化0为false
		c=c.length?c+' '+className:className;
		element.className=c;
	},
	removeClassName:function(element,className){
		if (!M.DOM.hasClassName(element,className)) {return};
		var c=element.className;
		var classes=c.split(/\s+/);//根据空白来将字符串分隔为数组
		for(var i=0,len=classes.length;i<len;i++){
			if (classes[i]==className) {
				classes.splice(i,1);//将符合要求的class删除
				break;
			};
		}
		element.className=classes.join('');
	},
	replaceNode:function(newNode,oldNode){
		var parent=oldNode.parentNode;
		if (newNode&&parent&&parent.nodeType==1) { //只有在父节点为元素节点情况下
			parent.insertBefore(newNode,oldNode);
			parent.removeChild(oldNode);
		};
	},
	removeElement:function(element){
		if (!element.parentNode) {return};
		element.parentNode.removeChild(element);
	},
	removeAllChildren:function(nodes){
		while(nodes.firstChild){ //只要存在第1个子节点就会一直运行下去
			nodes.removeChild(nodes.firstChild);
		}
	},
	show:function(elem){
		elem.style.display='block';
	},
	hide:function(elem){
		elem.style.display="none";
	},
	visible:function(elem){
		elem.style.visibility="visible";
	},
	hidden:function(elem){
		elem.style.visibility="hidden";
	},
	getStyle:function(elem,attr){
		if (elem.currentStyle) {
			return elem.currentStyle[attr];
		}else{
			return getComputedStyle(obj,false)[attr];
		}
	}
})

M.Event=new M.class({
	on:function(elem,d,b){
		//如果传入的是1个字符串，则将其转换为对象。
		if (typeof elem=='string') {
			elem=M.DOM.g(elem);
		}
		if (elem.addEventListener) {
			return elem.addEventListener(d,b,false);
		}else{
			if(elem.attachEvent){
				return elem.attachEvent('on'+d,b)
			}else{
				return elem['on'+d]=b;
			}
		}
	}
})

M.core=new M.class({
	isObject:function(unknow){
		//因为null也是1个特殊的对象,只有函数和对象才会返回true
		return (typeof unknow ==="function"||typeof unknow==='object'&&unknow!=null);
	},
	isNumber:function(unknow){
		return (typeof unknow ==="number"&&isFinite(unknow));
	}
})