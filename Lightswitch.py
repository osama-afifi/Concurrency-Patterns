class Lightswitch:

	def __init__(self):
		self.counter = 0
		self.mutex = Semaphore(1)

	def lock(self, mySem):
		self.mutex.wait()
		self.counter ++
		if self.counter == 1:
			mySem.wait()
		self.mutex.signal()

	def unlock(self, mySem):
		self.mutex.wait()
		self.counter --
		if self.counter == 0:
			mySem.signal()
		self.mutex.signal(