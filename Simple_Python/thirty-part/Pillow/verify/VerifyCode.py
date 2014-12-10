#! /usr/bin/env/python
#-*- coding:utf-8 -*-

from PIL import Image, ImageFont, ImageDraw
import random,sys


class VerifyCode:
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.mode = 'RGB'
		self.bgColor = (255,255,255)
		self.times = 4
		self.fontColor = (random.randint(0,255),random.randint(127,255),random.randint(0,127))
		self.lineColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.font = 'wqy.ttc'
		self.seed = u"我是一只小小鸟王菲红豆白天不懂夜的黑哥只是二个传说天空之城"
		self.im = Image.new(self.mode,(width,height),self.bgColor)


	def getSeed(self):
		self.str = []
		self.length = len(self.seed) - 1
		for t in range(0,self.times):
			x = random.randint(1,80)
			y = random.randint(1,30)
			self.str.append((x,y,self.seed[random.randint(0,self.length)]))

	def getLine(self):
		self.line = []
		for t in range(0,self.times):
			x1 = random.randint(1,80)
			x2 = random.randint(1,80)
			y1 = random.randint(1,30)
			y2 = random.randint(1,30)
			self.line.append(((x1,y1),(x2,y2)))

	def setFont(self):
		self.fnt = ImageFont.truetype(self.font,20)

	def draw(self):
		self.draw = ImageDraw.Draw(self.im)
		for x,y,c in self.str:
			self.draw.text((x,y),c,font=self.fnt,fill=self.fontColor)
		for x,y in self.line:
			self.draw.line([x,y],fill=self.lineColor,width=1)

	def generate(self):
		self.getSeed()
		self.getLine()
		self.setFont()
		self.draw()
		self.im.save('verify.png')

if __name__ == '__main__':
	verify=VerifyCode()
	verify.generate()