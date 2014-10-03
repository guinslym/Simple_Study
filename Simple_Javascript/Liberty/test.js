(function(){
	var Como = window.Como = function(selector, context){
	    var result = _find(selector, context);
	    if(result.length){
	        Como.Object.extend(result, _como_prototype);
	        return result;
	    } 
	        return null;
    };
    Como.version = "0.1.1";
    //原型
	var _como_prototype = {
	    //judge the object is a Como
	    como: true,
	    size: function () {
	        return this.length;
	    },
	    get: function (num){
	        return num == undefined ? this : Como(this[num]);
	    },
	    each: function (callback) {
	        for(var i = 0, il = this.length; i < il; i++) {
	            if(callback(Como(this[i]), i) == 'break') break;
	        }
	        return this;
	    },
	    collect: function(callback){
	        return Como.Array.collect(this, callback);
	    },
	    index: function(elem){
	        if(elem.size){
	            elem = elem[0];
	        }
	        return Como.Array.index(this, elem);
	    },
	    unique: function(){
	        return Como.Array.unique(this);
	    }
	};

    var _find = function(selector, context){
    if(selector == null) return [];
    if(selector instanceof Array){
        return selector;
    } else {
        if(typeof selector == 'object'){
            if(selector.nodeType){
                return [selector];
            } else if(selector.size){
                return selector;
            } else {
                return [selector];
            }
        } else {
            if(typeof selector != 'string'){ return []; }
            else{
                if(context && context.size && context.length) context = context[0];
                return mini(selector, context);
            }
        }
    }
    };

    var mini = (function(){
        var exprClassName = /^(?:[\w\-]+)?\.([\w\-]+)/,
            exprId = /^(?:[\w\-]+)?#([\w\-]+)/,
            exprNodeName = /^([\w\*\-]+)/,
            exprNodeAttr = /^(?:[\w\-]+)?\[([\w]+)(=(\w+))?\]/,
            na = [null,null, null, null];
        
        //寻找选择器及其上下文
        function _find(selector, context) {
            context = context || document;
            var simple = /^[\w\-#]+$/.test(selector);
            if (!simple && context.querySelectorAll) {//如果具有id的属性及支持HTML5选择器API，例如#my-box
                if(context.nodeType == 1){ //如果上下文为元素节点
                    var old = context.id, id = context.id = "__como__";
                    try {
                        return realArray(context.querySelectorAll( "#" + id + " " + selector ));
                    } catch(e) {
                    } finally {
                        if ( old ) {
                            context.id = old;//如果上下文具有id属性
                        } else {
                            context.removeAttribute( "id" );
                        }
                    }
                }
                return realArray(context.querySelectorAll(selector));          
            }
            if (selector.indexOf(',') > -1) {
                var split = selector.split(/,/g), ret = [], sIndex = 0, len = split.length;
                for(sIndex; sIndex < len; ++sIndex) {
                    ret = ret.concat(_find(split[sIndex], context));
                }
                return unique(ret);
            }
            selector = selector.replace(' > ', '>').replace('>', ' > ');
            var  parts = selector.split(/ /g),
                part = parts.pop(),
                id = (part.match(exprId) || na)[1],
                className = !id && (part.match(exprClassName) || na)[1],
                nodeName = !id && (part.match(exprNodeName) || na)[1],
                _attr = part.match(exprNodeAttr) || na,
                attrName = _attr[1] || null,
                attrValue =  _attr[3] || null,
                collection = !id && realArray(context.getElementsByTagName(nodeName || '*'));

            if (className) {
                collection = filterByAttr(collection, 'className', className);
            }
            if(attrName){
                collection = filterByAttr(collection, attrName, attrValue);
            }
            if (id) {
                var byId = context.getElementById(id);
                return byId?[byId]:[];
            }
         
            return parts[0] && collection[0] ? filterParents(parts, collection) : collection;
        }
        
        //转换为数组
        function realArray(c) {
            try {
                return Array.prototype.slice.call(c);//返回传入的参数个的数组，将其视为slice()即可
            } catch(e) {
                var ret = [], i = 0, len = c.length;
                for (i; i < len; ++i) {
                    ret[i] = c[i];
                }
                return ret;
            }
        }
        
        //根据其父类进行选择
        function filterParents(selectorParts, collection, direct) {
            var parentSelector = selectorParts.pop();
            if (parentSelector === '>') {
                return filterParents(selectorParts, collection, true);
            }
            var ret = [],
                r = -1,
                id = (parentSelector.match(exprId) || na)[1],
                className = !id && (parentSelector.match(exprClassName) || na)[1],
                nodeName = !id && (parentSelector.match(exprNodeName) || na)[1],
                cIndex = -1,
                node, parent,
                matches;
            nodeName = nodeName && nodeName.toLowerCase();
            while ( (node = collection[++cIndex]) ) {
                parent = node.parentNode;
                do {
                    matches = !nodeName || nodeName === '*' || nodeName === parent.nodeName.toLowerCase();
                    matches = matches && (!id || parent.id === id);
                    matches = matches && (!className || RegExp('(^|\\s)' + className + '(\\s|$)').test(parent.className));
                    if (direct || matches) { break; }
                } while ( (parent = parent.parentNode) );
                if (matches) {
                    ret[++r] = node;
                }
            }
            return selectorParts[0] && ret[0] ? filterParents(selectorParts, ret) : ret;
        }
        
        //参数的唯一性
        var unique = function(){
            var uid = +new Date();
            var data = function(){
                var n = 1;
                return function(elem) {
                    var cacheIndex = elem[uid],
                        nextCacheIndex = n++;
                    if(!cacheIndex) {
                        elem[uid] = nextCacheIndex;
                        return true;
                    }
                    return false;
                };
            }();
            return function(arr) {
                var length = arr.length,
                    ret = [],
                    r = -1,
                    i = 0,
                    item;
                for (i; i < length; ++i) {
                    item = arr[i];
                    if (data(item)) {
                        ret[++r] = item;
                    }
                }
                uid += 1;
                return ret;
            };
        }();
        
        //通过属性来选择元素
        function filterByAttr(collection, attr, value) {
            var reg = RegExp('(^|\\s)' + value + '(\\s|$)');
            var test = function(node){
                var v = attr == 'className' ? node.className : node.getAttribute(attr);
                if(v){
                    if(value){
                        if(reg.test(v)) return true;
                    } else {
                        return true;
                    }
                }
                return false;
            };
            var i = -1, node, r = -1, ret = [];
            while ( (node = collection[++i]) ) {
                if (test(node)) {
                    ret[++r] = node;
                }
            }
            return ret;
        }
        return _find;
    })();

    Como.Object = {
    /*
     * 拓展对象
     */
    extend: function (target,src) { //对目标对象进行继承其
        for (var it in src) {
            target[it] = src[it];
        }
        return target;
    },
    /*
     * 循环对象
     */
    each: function (obj, cb) {
        var i = 0;
        for (var it in obj) {
            if(cb(obj[it], it ,i++)=='break') break;
        }
        return obj;
    },

    /*
     * 深层次复制对象
     */
     clone: function(obj){
        var con = obj.constructor, cloneObj = null;
        if(con == Object){
            cloneObj = new con();
        } else if (con == Function){
            return Como.Function.clone(obj);
        } else cloneObj = new con(obj.valueOf());

        for(var it in obj){
            if(cloneObj[it] != obj[it]){
                if(typeof(obj[it]) != 'object'){
                    cloneObj[it] = obj[it];
                } else {
                    cloneObj[it] = arguments.callee(obj[it])
                }
            }
        }
        cloneObj.toString = obj.toString;
        cloneObj.valueOf = obj.valueOf;
        return cloneObj;
     },
    };
    window.$ = Como;//提供给外界的简写接口
})();