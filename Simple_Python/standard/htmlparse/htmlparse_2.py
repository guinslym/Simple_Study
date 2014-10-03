#coding:utf-8
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attr):
        print "Encountered a start tag:",tag
    def handle_endtag(self,tag):
        print "Encountered an end tag:",tag
    def handle_data(self,data):
        print "Encountered some data:",data
    def handle_decl(self,data):
        print "Decl:",data
    def handle_charref(self,name):
        if name.startswith("x"):
            c=unichr(int(name[1:],16))
        else:
            c=unichr(int(name))
        print "Num ent:",c
    def handle_comment(self,data):
        print "Comment:",data

parser=MyHTMLParser()
data=file("115.html").read().decode("utf-8")
parser.feed(data)
parser.close()
