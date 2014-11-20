# Osama M. Afifi osama.egt@gmail.com -  20/Nov/2014
#
# FIFO Semaphore Concurrency Pattern
#
# We want semaphores to wait/signal in a FIFO manner by using a thread-safe Queue
# This code is deadlock free if you can see anything else feel free to tell me

class FifoQueue:
	def __init__(self):
		self.queue = Queue()
		self.mutex = Semaphore(1)
		self.hasElements = Sempahore(0)

	def wait():
		self.mutex.wait()
		self.queue.add(mySem)
		self.mutex.signal()
		mySem.wait()
		hasElements.signal()

	def signal():
		hasElements.wait()
		self.mutex.wait()
		mySem = self.queue.remove()
		self.mutex.signal()
		mySem.signal()
		