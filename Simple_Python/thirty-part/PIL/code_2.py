#coding:utf-8
from PIL import Image, ImageDraw, ImageFont
FONT = ImageFont.truetype("simple.ttf",24)
img = Image.new("1",(200,50),"white")
draw = ImageDraw.Draw(img) #调用画笔，开始作画，在img这个画布上画吧
draw.text((0,0),"hello world",font=FONT) #在坐标(0,0)开始画
img.show()