import pycurl

c = pycurl.Curl()
# Redirects to https://www.python.org/.
c.setopt(c.URL, 'http://www.python.org/')
# Follow redirect.
c.setopt(c.FOLLOWLOCATION, True)
c.perform()
c.close()