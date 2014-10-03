Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from urlparse import urlparse
>>> url="http://netloc/path;param?query=arg#frag"
>>> parsed=urlparse(url)
>>> print parsed
ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=arg', fragment='frag')
>>> 
