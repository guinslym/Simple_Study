#coding:utf-8
from PIL import Image, ImageDraw, ImageFont
import random
width=100
height=40
bgcolor=(255,255,255)
char="abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
length=len(char)-1
time=4
s=[]
x_list=[]
y_list=[]
linecolor = (0,0,0)

img = Image.new("RGB",(width,height),bgcolor)
FONT = ImageFont.truetype("simple.ttf",32)
FONT_COLOR = (0,0,0)
draw = ImageDraw.Draw(img) 
for i in xrange(1,time+1):
	x=random.randint(0, 70)
	y=random.randint(0, 20)
	x_list.append(x)
	y_list.append(y)
	s.append((x,y,char[random.randint(0,length)]))
for x,y,c in s:
	draw.text((x,y),c,font=FONT,fill=FONT_COLOR)
for x in xrange(0,3):
	x1 = random.randint(0,width)
	x2 = random.randint(0,width)
	y1 = random.randint(0,height)
	y2 = random.randint(0,height)
	draw.line([(x1,y1),(x2,y2)],linecolor)
img.save("code_4.png")