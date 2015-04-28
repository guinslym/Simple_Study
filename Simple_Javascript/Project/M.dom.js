(function(){
    var M = function(){
        return new M.fn.init();  //调用原型方法init(),实例化init初始化类型,分隔作用域
    };
    M.fn = M.prototype = {
        'version':0.1,
        init:function(){
            return this;
        },
        dom:function(selector,context){
            selector = selector || document;
            context = context || document;
            if (document.querySelectorAll) {
                var len = context.querySelectorAll(selector).length;
                if(len>1){
                    this.dom= context.querySelectorAll(selector);
                    this.dom.length = len;
                }else{
                    this.dom = context.querySelector(selector);
                     this.dom.length = 1;
                }
            }else{
                var len = context.getElementsByTagName(selector);
                if(len>1){
                    this.dom = context.getElementsByTagName(selector);
                    this.dom.length = len;
                }else{
                    this.dom = context.getElementsByTagName(selector)[0];
                    this.dom.length = 1;
                }
            }
            return this;
        },
       css:function(data){
         for (var i = 0; i < this.dom.length; i++) {
            for(var prop in data){
                    this.dom[i].style[prop]=data[prop];
                }
         };
         return this;
       }
    };
    M.fn.init.prototype = M.fn;//使用原型对象覆盖init的原型对象
    M.extend = M.fn.extend = function(obj){
        for(var prop in obj){
            this[prop] = obj[prop]
        }
        return this;
    }
    window.M = new M();
})();