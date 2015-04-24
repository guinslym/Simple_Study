(function(){
       function M(){};
       M.prototype.dom = function(elem){
          var delimeter = elem.charAt(0);
          switch(delimeter){
            case '#':
                return M.prototype.id(elem);
            break;
            case '.':
                return M.prototype.c(elem);
            break;
            default:
               return M.prototype.tag(elem);
            break;
          }
       };
       //获取id的函数
       M.prototype.id = function(elem){
          if(document.querySelector){
            return document.querySelector(elem);
          }else{
            elem = elem.substr(1);
            return document.getElementById(elem);
          }
       }
       //获取类名的函数
       M.prototype.c = function(elem){
         if(document.querySelectorAll){
            var len = document.querySelectorAll(elem).length;
            if (len>1){
                return document.querySelector(elem);
            }else{
                return document.querySelector(elem);
            }
         }else{
            elem = elem.substr(1);
            var len = document.getElementsByClassName(elem).length;
            if(len>1){
                 return document.getElementsByClassName(elem);
            }else{
                 return document.getElementsByClassName(elem)[0];
            }
         }
       }
       M.prototype.tag = function(elem){
        if (document.querySelectorAll) {
            var len = document.querySelectorAll(elem).length;
            if(len>1){
                return document.querySelectorAll(elem);
            }else{
                return document.querySelector(elem);
            }
        }else{
            var len = document.getElementsByTagName(elem).length;
            if(len>1){
                return document.getElementsByTagName(elem);
            }else{
                return document.getElementsByTagName(elem)[0];
            }
        }
       }
       //实例化1个原型
       window.M = new M();
})();

//调用方式
//M.dom('#upload').onclick=function(){alert(1111)}
//扩展的方式是直接M.xxx,其中xxx代表函数名,再写1个对应的函数名即可
// M.alert=function(){
//     document.body.style.background='green';
// }
// M.alert()