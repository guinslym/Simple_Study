function ajax(url, fnSucc, fnFaild)//创建1个ajax函数，该函数有3个参数，url,连接成功时的函数，连接失败时的函数
{
	//1.创建1个Ajax对象
	if(window.XMLHttpRequest)//如果存在则执行该行
	{
		var oAjax=new XMLHttpRequest();
	}
	else
	{
		var oAjax=new ActiveXObject("Microsoft.XMLHTTP");
	}
	
	//2.连接服务器（打开和服务器的连接）
	oAjax.open('GET', url, true);
	
	
	//3.发送请求
	oAjax.send();
	
	//4.接收返回值
	oAjax.onreadystatechange=function ()
	{
		if(oAjax.readyState==4)
		{
			if(oAjax.status==200)
			{
				//alert('成功了：'+oAjax.responseText);
				fnSucc(oAjax.responseText);
			}
			else
			{
				//alert('失败了');
				if(fnFaild)
				{
					fnFaild(oAjax.statusText);
				}
			}
		}
	};
}