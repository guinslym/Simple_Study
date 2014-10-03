#coding:utf8
import xml.etree.ElementTree as ET

root = ET.Element("booklist")
def add_book(id,mytitle,myfirst,mylast,mydate):
    
    book = ET.SubElement(root,"book")
    title = ET.SubElement(book,"title")
    author = ET.SubElement(book,"author")
    name = ET.SubElement(author,"name")
    first_name =ET.SubElement(name,"firstname")
    last_name =ET.SubElement(name,"lastname")
    pubdate =ET.SubElement(book,"pubdate")
    

    #加入文本节点
    title.text=mytitle
    first_name.text=myfirst
    last_name.text=mylast
    pubdate.text=mydate
    book.set("id",id)
    
    #生成文件
    tree=ET.ElementTree(root)
    tree.write("book2.xml",encoding="UTF-8")

add_book("1001","An apple","Peter","Zhang","2014-1-2")
add_book("1002","Love",  "Mike", "Li", "2013-11-2")
add_book("1003", "Steve.Jobs", "Tom", "Wang", "2014-4-2")
add_book("1004", "Harry Potter", "Peter","Chen","2013-10-2")

