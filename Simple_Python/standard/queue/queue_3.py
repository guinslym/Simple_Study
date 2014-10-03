import Queue
import threading
class Job(object):
	"""docstring for Job"""
	def __init__(self, priority,description):
		self.priority = priority
		self.description = description
		print "New Job:",description
		return
	def __cmp__(self,other):
		return cmp(self.priority,other.priority)
		
q=Queue.PriorityQueue()
q.put(Job(3,"Mid-level job"))
q.put(Job(30,"Low-level job"))
q.put(Job(13,"Important job"))

def process_job(q):
	while True:
		next_job=q.get()
		print "Processing Job:",next_job.description
		q.task_done()
worker=[threading.Thread(target=process_job,args=(q,)),
        threading.Thread(target=process_job,args=(q,)),
        ]
for w in worker:
	w.setDaemon(True)
	w.start()

q.join()