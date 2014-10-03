var M_event={
	stopBubble:function(e){
		if (e&&e.stopPropagation) {
			e.stopPropagation();
		}else{
			window.event.cancelBubble=true;
		}
    },
    stopDefault:function(e){
		if (e&&e.preventDefault) {
			e.preventDefault();
		}else{
			window.event.returnValue=false;
		}
		return false;
    },
    addHandler:function(elem,type,handler){
    	if(elem.addEventListener){
    		elem.addEventListener(type,handler,false);
    	}else if (elem.attachEvent) {
    		elem.attachEvent("on"+type,handler);
    	}else{
    		elem["on"+type]=handler;
    	}
    },
    removeHandler:function(elem,type,handler){
    	if (elem.removeEventListener) {
    		elem.removeEventListener(type,handler,false);
    	}else if (elem.detachEvent) {
    		elem.detachEvent('on'+type,handler);
    	}else{
    		elem['on'+type]=null;
    	}
    },
    getEvent:function(e){
    	return e ? e : window.e;
    },
    getTarget:function(e){
    	return e.target||e.srcElement;
    },
    getElementLeft:function(elem){ //获取元素外围左侧偏移量
		var actualLeft=elem.offsetLeft;
		var current=elem.offsetParent;
		while(current !==null){
			actualLeft +=current.offsetLeft;
			current=current.offsetParent;
		}
		return actualLeft;
    },
    getRelatedTarget:function(){
    	if (event.relatedTarget) {
    		return event.relatedTarget;
    	}else if (event.toElement) {
    		return event.toElement;
    	}else if (event.fromElement) {
    		return event.fromElement;
    	}else{
    		return null;
    	}
    },
    getElementTop:function(elem){ //获取元素外围的高度
		var actualTop=elem.offsetTop;
		var current=elem.offsetParent;
		while(current!==null){
			actualTop+=current.offsetTop;
			current=current.offsetParent;
		}
		return actualTop;
    },
    getCharCode:function(e){
    	if (typeof e.charCode == 'number') {
    		return e.charCode;
    	}else{
    		return e.keyCode;
    	}
    },
    getViewport:function(){ //获取可视区的宽高
    	if (document.compatMode=="BackCompat") {
    		return {
    			width:document.body.clientWidth,
    			height:document.body.clientHeight
    		};
    	}else{
    		return {
    			width:document.documentElement.clientWidth,
    			height:document.documentElement.clientHeight
    		};
    	}
    },
    set:function(elem,attr,option){
        return elem.setAttribute(attr,option);
    }
};
