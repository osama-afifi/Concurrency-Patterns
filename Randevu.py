# Osama M. Afifi osama.egt@gmail.com - 19/Nov/2014
#
# Randevu Concurrency Pattern
#
# We want two threads to synchronize at a certain execution point i.e meet/randevu
#
# The two statements A and B and we want both statements execute sych that each finish their first statement first and wait for each other
# in the middle to continue executing their second statements. 
# This code is deadlock free


# You should fill up your own statements here
def aFirstStatement():
	pass

def aSecondStatement():
	pass

def bFirstStatement():
	pass

def bSecondStatement():
	pass


aArrived = Semaphore(0)
bArrived = Semaphore(0)


def randevuA():
	aFirstStatement()
	aArrived.signal()
	bArrived.wait()
	aSecondStatement()
	
def randevuB():
	bFirstStatement()
	bArrived.signal()
	aArrived.wait()
	bSecondStatement()
	