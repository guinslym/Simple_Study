# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:39:08 2015

@author: tim
"""

import functools

class Math(object):
    def Factorial(self,n):
        """计算给定数值的阶乘结果"""
        if not self._isInt(n) or n<0:
            raise ValueError('Function Factorial only accepts integral values')
        if n in range(0,3):
            print n
            return n
        else:
            num = 1
            for x in range(2,n+1):
                num *= x
            return num
    def _isInt(self,n):
        """判断1个数值是不是整数"""
        return isinstance(n,int)
    def Binomial(self,n,m):
        """计算二项式乘积"""
        if not (self._isInt(m) or self._isInt(n)):
            raise ValueError('Function Binomial only accepts integral values')
        if n<m:
            raise ValueError('Argument n moust be greater than m')
        elif (n-m) in [0,1]:
            return self.Factorial(n)
        elif m == 0:
            return 1
        elif m == 1:
            return n
        else:
            m = n-m
        return functools.reduce((lambda x,y:x*y),range(n,m,-1))

m = Math()
print m.Binomial(4,2)