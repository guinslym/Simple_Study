#coding:utf-8
from PIL import Image, ImageDraw
img = Image.new("1",(100,100),"white")
draw = ImageDraw.Draw(img) #调用画笔，开始作画
draw.text((0,0),"hello world")
img.show()