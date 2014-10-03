#coding:utf-8
from PIL import Image, ImageDraw
img = Image.new("1",(200,50),"white")
draw = ImageDraw.Draw(img) #调用画笔，开始作画，在img这个画布上画吧
draw.line(((0,0),(100,200))) #花几条杠杠，耍一下OCR识别
img.show()