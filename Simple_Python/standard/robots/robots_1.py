#! /usr/bin/env/python
# -*- coding:utf-8 -*

import robotparser
import urlparse

AGENT_NAME = 'PyMOTW'
URL_NAME = 'http://www.jd.com/'
parser = robotparser.RobotFileParser()
parser.set_url(urlparse.urljoin(URL_NAME,'robots.txt'))
parser.read()

PATHS = [
    '/',
    '/pinpai/',
    '/admin/',
    '/help/question-881.html',
]

for path in PATHS:
    print '%6s: %s' % (parser.can_fetch(AGENT_NAME,path),path)
    url = urlparse.urljoin(URL_NAME,path)
    print '%6s:%s' % (parser.can_fetch(AGENT_NAME,url),url)
    print