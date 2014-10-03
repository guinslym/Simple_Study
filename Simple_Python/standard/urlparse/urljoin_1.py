import urlparse
url="http://www.python.org/doc/FAQ.html"
new="current/lib/lib.html"
a=urlparse.urljoin(url,new)
print a