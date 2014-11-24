class Lightswitch:

	def __init__(self):
		self.counter = 0
		self.mutex = Semaphore(1)

	def lock(self, semaphore):
		self.mutex.wait()
		self.counter ++
		if self.counter == 1:
			semaphore.wait()
		self.mutex.signal()

	def unlock(self, semaphore):
		self.mutex.wait()
		self.counter --
		if self.counter == 0:
			semaphore.signal()
		self.mutex.signal(