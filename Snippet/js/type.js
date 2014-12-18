
/*
用于给定参数的类型
 */
function type(obj){
	return Object.prototype.toString.call(obj);
}
/*
 判断传入的参数是否是1个函数，返回true或false.
 */
function isFunction(obj){
	return type(obj)==="[object Function]";
}

/*
判断1个对象是否为空对象
 */
function isNull(obj){
	return type(obj)==="[object Null]";
}
/*
判断给定的参数是否是1个对象，返回true或false.
 */
function isObject(obj){
	return type(obj)===("[object Object]")||isNull(obj);
}

/*
判断1个对象是否是数组对象，利用Array.isAarray()方法或Array的实例对象来判断
 */
function isArray(object){
	return object instanceof Array||Array.isArray(object);
}

/*
判断1个对象是否是数字对象
 */
function isNumber(obj){
	return type(obj)==="[object Number]";
}

/*
判断1个对象是否是字符串对象
 */
function isString(obj){
	return type(obj)==="[object String]";
}
