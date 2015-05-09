/*
 *缓存函数,使用数组来存储请求url的数据
 */
function Cache(url,data){
    var Cache = [];
    if (typeof(Cache[url]=='undefined')) {
        Cache[url]=data;
    }else{
        document.body.HTMLText = Cache[url];
    }
}