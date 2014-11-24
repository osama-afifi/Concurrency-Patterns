# Osama M. Afifi osama.egt@gmail.com -  25/Nov/2014
#
# No-Starve Reader Writer Concurrency Pattern
#
# A Multiple Reader Single Writer exclusive access used on databases, file-systems and many other datastructures.
# This Version ensures that the Writer thread never starves by using a turnstile before writing to block further readers to enter the reading section
# This code can be shortened by using a Light-switch object which you can find also in this repository.
# This code is deadlock free if you can see anything else feel free to tell me.

roomEmpty = Semaphore(1)
turnstile = Semaphore(1)
mutex = Semphore
readerCounter = 0


def Writer():
	while True:
		turnstile.wait()
		roomEmpty.wait()
		# Writer Critical Writing goes here.
		roomEmpty.signal()
		turnstile.signal()

def Reader():
	while True:
		turnstile.wait()
		turnstile.signal()
	
		# Light-switch can be replaced by object
		mutex.wait()
		readerCounter++
		if(readerCounter==1):
			roomEmpty.wait() # Light-switch On
		mutex.signal()
		
		# Reader Critical Reading goes here.
		
		mutex.wait()
		readerCounter--
		if(readerCounter==0):
			roomEmpty.signal() # Light switch Off
		mutex.signal()
	
		