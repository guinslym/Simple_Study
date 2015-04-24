# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:27:44 2015
关于cookie的设置和读取
@author: tim
"""

import Cookie

class HTTPCookie:
    def __init__(self):
        self.c = Cookie.SimpleCookie()
        self.cookie_info = dict()

    def setCookie(self,name,value,**kargs):
        """设置cookie"""
        self.c[name]=value
        for key in kargs.keys():
            if key in ['expires','max-age']:
                self.c[name][key] = kargs[key] 
    
    def getCookie(self,name=None):
        """获取Cookie"""
        if name is None:
            for keys,values in self.c.iteritems():
                self.cookie_info[keys]=values.value
            return self.cookie_info
        else:
            if self.c.has_key(name):
                return self.c.get(name).value
            else:
                return 'Has not key:{}'.format(name)
    def output(self):
        """输出Cookie头信息"""
        return self.c
    def js_output(self,attr=None):
        """输出js的cookie代码"""
        if attr is None:
            return self.c.js_output(attrs=[])
        else:
            return self.c.js_output(attr)
            

if __name__ == '__main__':
    m=HTTPCookie()
    m.setCookie('age',20)
    m.setCookie('name','zhangsan')
    m.setCookie('sex','male',expires=30)
    print m.getCookie()
    print m.getCookie('name')
    print m.js_output('max-age')