from bs4 import BeautifulSoup

html_doc = file("115.html").read()

soup =BeautifulSoup(html_doc)
'''for child in soup.find_all("div"):
    line=child.string
    print line'''
for child in soup.find_all("div",class_="section-title"):
    line=child.string
    print line
