#coding:utf-8
class Book(object):
	"""主要是创建类及实例化类"""

	def __init__(self,nm,ph):
		super(Book, self).__init__()
		self.name = nm
		self.phone = ph
		print 'Create instance for:',self.name

	def updatePhone(self,newph):
		self.phone=newph
		print 'Updated phone# for:',self.name
		print 'Updated phone# to',self.phone

class Address(Book):
	"""主要是继承于Book类，并实现自己的一些方法"""
	def __init__(self, nm, ph, id, em):
		Book.__init__(self,nm,ph)
		self.empid = id
		self.email = em

	def updateEmail(self,newem):
	 	self.email = newem
	 	print 'Updated e-mail address for:',self.name
	 	print 'Updated e-mail address to:',self.email
		
if __name__ == '__main__':
	jo=Address('John Doe','408-555-1212',99,'john@163.com')
	ja=Address('Jane Mike','020-6722333',168,'jane@126.com')
	jo.updatePhone('123456')

	#jo.name
	#jo.phone
	#jo.empid
	#jo.email
