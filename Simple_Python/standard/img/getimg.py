import re
import urllib

def get_html(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def get_img(html):
    reg=r'src="(.*?\.jpg)" width'
    imgre=re.compile(reg)
    img_list=imgre.findall(html)
    x=0
    for img_url in img_list:
        urllib.urlretrieve(img_url,"%s.jpg" % x)
        x+=1


url="http://xiangce.baidu.com/square/67399903"
html=get_html(url)
get_img(html)
