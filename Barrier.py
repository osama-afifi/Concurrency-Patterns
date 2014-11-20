# Osama M. Afifi osama.egt@gmail.com - 19/Nov/2014
#
# Barrier Concurrency Pattern
#
# We want N threads to synchronize at a certain execution point 
#
# The N statements pass the first turnstile and the last thread locks the first turnstile and unlocks the second turnstile
# in the second phase the last thread locks the second turnstile and unlocks the first
# in my implementation I assume semaphore signal takes the number of signals as a parameter
# This code is deadlock free if you can see anything else feel free to tell me

class Barrier:
	def __init__(self, n):
	self.n = n
	self.count = 0
	self.mutex = Semaphore(1)
	self.turnstile = Semaphore(0)
	self.turnstile2 = Semaphore(0)

	def phase1(self):
	self.mutex.wait()
	self.count += 1
	if self.count == self.n:
		self.turnstile.signal(self.n)
	self.mutex.signal()
	self.turnstile.wait()

	def phase2(self):
	self.mutex.wait()
	self.count -= 1
	if self.count == 0:
		self.turnstile2.signal(self.n)
	self.mutex.signal()
	self.turnstile2.wait()

	def wait(self):
	self.phase1()
	self.phase2()