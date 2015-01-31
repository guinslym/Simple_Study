#! /usr/bin/env/python
# -*- coding:utf-8 -*-

#底盘进入装配线需要的时间
e1=2
e2=4

#底盘离开装配线需要的时间
s1=3
s2=2

#底盘在装配线上每个装配站的处理时间
a1=[7,9,3,4,8,4]
a2=[8,5,6,4,5,7]

#底盘在装配件之间移动需要的时间
t1=[2,3,1,3,4]
t2=[2,1,2,2,1]

#初始化f1和f2,也就是进入装配线时间和第1个装配站用时之和
f1=[e1+a1[0]]
f2=[e2+a2[0]]

#dp方式,分别计算2条装配线的最短时间装配时间
i=1
l1=[]
l2=[]
while i<6:
    if (f1[i-1]+a1[i])<(f2[i-1]+a1[i]+t2[i-1]):
        f1.append(f1[i-1]+a1[i])
        l1.append(1)
    else:
        f1.append(f2[i-1]+a1[i]+t2[i-1])
        l1.append(2)

    if (f2[i-1]+a2[i]) <(f1[i-1]+a2[i]+t1[i-1]):
        f2.append(f2[i-1]+a2[i])
        l2.append(2)
    else:
        f2.append(f1[i-1]+a2[i]+t1[i-1])
        l2.append(1)
    i +=1

#离开装配站
f1.append(f1[-1]+s1)
f2.append(f2[-1]+s2)

print f1
print f2
print l1
print l2