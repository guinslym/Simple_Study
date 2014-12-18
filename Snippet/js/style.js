/*
设置1个节点的属性,如果不给定属性值，则删除该节点属性，否则添加属性和属性值
 */
function setAttr(node,name,value){
	value==null ? node.removeAttribute(name) : node.setAttribute(name,value);
}

/*
获取节点的class属性名
 */
function getClassName(node){
	return node.getAttribute('class')||node.className;
}

/*
为1个节点添加1个class,首先判断节点是否存在classList属性，如果没有则获取到节点原先的类名，然后再将传入的类名追加到后面。
 */
function addClass(node,value){
	if (node.classLists) {
		node.classList.add(value);
	}else{
		var className=getClassName(node)+" "+value;
	    node.className=className;
	}
}

/*
获取节点的内容或设置其内容
 */
function val(node,value){
	if (value==null) {
		return node.textContent;
	}else{
		if(node.nodeType==1){
		node.innerHTML=value;
	    }
	}
}

/*
对传入的字符串进行去除空格操作
 */
function trim(str){
	return str==null ? "" : String.prototype.trim.call(str);
}

/*
获取父元素下的子元素
 */
function children(parentNode){
	if(parentNode.childNodes){
		return parentNode.childNodes;
	}else if(parentNode.children){
		return parentNode.children;
	}
}

function childCount(parentNode){
	if (parentNode.childElementCount) {
		return parentNode.childElementCount;
	}else{
		return children(parentNode).length;
	}
}