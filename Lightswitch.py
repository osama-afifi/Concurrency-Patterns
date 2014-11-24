# Osama M. Afifi osama.egt@gmail.com -  24/Nov/2014
#
# Lightswitch Pattern
#
# A Simple Pattern which simulates a room where the first one who enter the room switches the light (signals the semaphore)
# and the last thread which leaves the room switch off (releases the semaphore)
# This code is deadlock free if you can see anything else feel free to tell me.

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