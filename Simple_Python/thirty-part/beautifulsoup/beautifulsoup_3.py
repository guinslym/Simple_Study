#coding:utf-8
from bs4 import BeautifulSoup

html_doc = file("1.htm").read()

soup =BeautifulSoup(html_doc)
'''for child in soup.find_all("div"):
    line=child.string
    print line'''
for children in soup.find_all("div",class_="infocon"):
    for child in children.find_all("p"):
        print child.get_text()
