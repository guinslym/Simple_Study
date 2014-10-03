#coding:utf-8
from bs4 import BeautifulSoup
import urllib

def html(url):
    #html_doc = file(url).read()
    html_doc=urllib.urlopen(url).read().decode("utf-8")

    soup =BeautifulSoup(html_doc)
    for children in soup.find_all("div",class_="infocon"):
        for child in children.find_all("p"):
            print child.get_text()  

html("http://www.360kad.com/product/3366.shtml")
html("http://www.360kad.com/product/12641.shtml")
html("http://www.360kad.com/product/596.shtml")
