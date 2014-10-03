#coding:utf8
import xml.etree.ElementTree as etree

tree=etree.parse("book.xml")
root=tree.getroot()

f = open("book.xml")
xml = f.read()
#以字符串的方式读取文件
parent = etree.fromstring(xml)
for children in parent:
    print children.tag,":",children.get("id")
    for childs in children:
        if childs.tag=="author":
            for name in childs.findall("name"):
                first=name.find("firstname").text
                last=name.find("lastname").text
                childs.text=first+"-"+last
        print childs.tag,":",childs.text   
    print "-"*30
