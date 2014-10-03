#coding:utf-8
import urllib
import json

url="http://www.weather.com.cn/data/sk/101280101.html"
data=urllib.urlopen(url)
line=data.readline().decode("utf-8")
j=json.loads(line)
info=j["weatherinfo"]
print u"城市City: %s" %info["city"]
print u"时间time:%s" %info["time"]
print u"风力wind-force: %s" %info["WS"]
print u"温度temperature: %s" %info["temp"]
