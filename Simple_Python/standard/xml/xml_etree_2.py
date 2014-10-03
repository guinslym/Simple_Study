#coding:utf8
#导入文件
import xml.etree.ElementTree as ET

#插入元素节点
root = ET.Element("booklist")
book = ET.SubElement(root,"book")
title = ET.SubElement(book,"title")
author = ET.SubElement(book,"author")
name = ET.SubElement(author,"name")
first_name =ET.SubElement(name,"firstname")
last_name =ET.SubElement(name,"lastname")
pubdate =ET.SubElement(book,"pubdate")

#加入文本节点
title.text="An apple"
first_name.text="Peter"
last_name.text="Zhang"
pubdate.text="2014-1-2"
book.set("id","1001")

#生成文件
tree=ET.ElementTree(root)
tree.write("book1.xml")


