#coding:utf-8
from PIL import Image
image = Image.open("wanted.jpg")
#距离上下，宽高
region = (100,200,400,500)
cropImg = image.crop(region)
cropImg.save("3.jpg")
