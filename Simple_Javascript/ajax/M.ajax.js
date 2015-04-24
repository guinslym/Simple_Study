/*
 * ajax处理的函数,需要传入1个对象类型
 * @param type,请求的类型
 * @param url,请求的url地址
 * @param dataType,请求的数据类型
 * @param data,发送的数据
 * @param success,成功的回调函数
 * @param error,错误的回调函数
 */
M.ajax=function(elem){
  if(arguments.length==1){
    var type,url,data,dataType;
    type = elem['type'];
    switch(type){
      case 'get':
        data = null;
      break;
      case 'post':
      if (elem['data']!==undefined){
        data = new FormData();
        for(var x in elem['data']){
          data.append(x,elem['data'][x]);
        }
      }
      break;
    }
    url = elem['url'];
    dataType = elem['dataType'];
    success_fn = elem['success'];
    error_fn = elem['error'];
    M._ajax(type,url,data,dataType,success_fn,error_fn);
  }else{
    console.log('The argument length must be 1');
  }
}
/*
 * ajax内部处理的函数
 * @param type,请求的类型
 * @param url,请求的url地址
 * @param dataType,请求的数据类型
 * @param data,发送的数据
 * @param success,成功的回调函数
 * @param error,错误的回调函数
 */
M._ajax=function(type,url,data,dataType,success,error){
  if (arguments.length>=3) {
    if(window.XMLHttpRequest){
      var xhr = new XMLHttpRequest();
    }else{
      var xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    if (dataType===undefined) {
      dataType = 'text';
    }
    xhr.open(type,url);
    xhr.send(data);
    xhr.onreadystatechange=function(){
      if(xhr.readyState==4){
        if (xhr.status==200) {
          var data_type = M._getDataType(xhr,dataType);
          success(data_type);
        }else{
          error(xhr.statusText);
        }
      }
    }
  };
}
/*
 * ajax内部获取输出对象的方式
 * @param xhr,XMLHTttpRequest对象
 * @param type,返回的数据类型
 */
M._getDataType = function(xhr,type){
  switch(type){
    case 'text':
       return xhr.responseText;
       break;
    case 'json':
       return JSON.parse(xhr.responseText);
       break;
    case 'xml':
       return xhr.responseXML;
       break;
    default:
      return xhr.responseText;
      break;
  }
}

// 调用方式
//M.ajax({
//     'type':'get',
//     'url': 'http://localhost/jd/test/info.php',
//     'data':{'name':'zhangsan','age':20},
//     'dataType':'text',
//     success:function(data){
//       alert(data);
//     },
//     error:function(data){
//       alert(data);
//     }
//   });