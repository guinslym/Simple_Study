import threading
from time import sleep,ctime

loops=[4,2]
class ThreadFunc(object):
	"""docstring for ThreadFunc"""
	def __init__(self, func,arg,name=""):
		self.name=name
		self.func=func
		self.arg = arg

	def __call__(self):
			apply(self.func,self.arg)

def loop(nloop,nsec):
	print "Start loop",nloop,"at:",ctime()
	sleep(nsec)
	print "loop",nloop,"done at:",ctime()

def main():
	print "Starting at:",ctime()
	threads=[]
	nloops=range(len(loops))

	for i in nloops:
		t=threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()
	print "All Done at:",ctime()

if __name__ == '__main__':
	main()