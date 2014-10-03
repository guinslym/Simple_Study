__author__ = 'Dog'
# -*- coding:utf-8 -*-

import urllib2
import random

url = "http://blog.csdn.net/happydeer"

my_headers = [
    "Mozilla/5.0 (Window NT 6.1;WOW64;rv:27.0) Gecko/20100101 Firefox/27.0",
    "Mozilla/5.0 (Window;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6",
    "Mozilla/5.0 (X11;Ubuntu;Linux i686;rv:10.0) Gecko/20100101 Firefox/1.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
]


def get_content(url, headers):
    """
    @获取403禁止访问的网页页面
    """
    random_header = random.choice(headers)
    req = urllib2.Request(url)
    req.add_header("User-Agent", random_header)
    req.add_header("Host", "blog.csdn.net")
    req.add_header("GET", url)
    req.add_header("Refer", "http://blog.csdn.net/")

    content = urllib2.urlopen(req).read().decode("utf-8")
    return content

print get_content(url,my_headers)
