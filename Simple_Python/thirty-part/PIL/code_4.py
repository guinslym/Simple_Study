#coding:utf-8
from PIL import Image, ImageDraw, ImageFont
FONT = ImageFont.truetype("simple.ttf",24)
img = Image.new("1",(200,50),"white")
draw = ImageDraw.Draw(img) #调用画笔，开始作画，在img这个画布上画吧
draw.text((5,5),"h",font=FONT)
draw.line(((0,0),(100,50))) #花几条杠杠，耍一下OCR识别
draw.text((105,15),"e",font=FONT)
draw.line(((150,30),(40,50))) 
img.show()