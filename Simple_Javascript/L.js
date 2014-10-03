(function(window){
	var core_VERSION=0.11,
	rootElem,
	Lib=function(selector,context){
		return new Lib.fn.init(selector,context,rootElem);
	};
	
	//为后面的引用做准备
	Lib.fn=Lib.prototype={
		version:core_VERSION,
		constructor:Lib,
		init:function(selector,context,rootElem){
			if (!selector) {return this;}
			switch(typeof selector){
				case 'string':
				    switch (selector.charAt(0)){
				    	case '#':
				    	    this.elem=document.getElementById(selector.substring(1));
				    	    this.context=document;
				    	    return this;
				    	    break;
				    	case '.':
				    	    this.elem=document.getElementsByClassName(selector.substring(1));
				    	    return this;
				    	    break;
				    	default:
				    	    this.elem=document.getElementsByTagName(selector);
				    	    return this;
				    }
				    break;
				case 'function':
				    break;
				case 'object':
				    this.elem=selector;
				    return this;
			}
		},
	}

	//让Lib.fn.init与Lib产生引用关系，可以借此操作其后面的方法
	Lib.fn.init.prototype=Lib.fn;

	//提供对外的接口
	window.L=window.Lib=Lib;
})(window)