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

if __name__ == '__main__':
	john=Book('John Doe','408-555-1212')
	jane=Book('Jane Mike','020-6722333')
