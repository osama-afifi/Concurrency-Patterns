# Osama M. Afifi osama.egt@gmail.com -  20/Nov/2014
#
# Exclusive Concurrency Pattern
#
# We have two queues Leader & Followers and want both doSomething() together where each leader must have a corresponding follower
# This code is deadlock free if you can see anything else feel free to tell me

mutex = Semaphore(1)
randevu = Semaphore(0)
followerQueue = Semaphore(0)
leaderQueue = Semaphore(0)
followers = 0
leader = 0


def doSomething():
	pass

def leaderStatment():
	mutex.wait()
	if followers>0:
		followers--
		followerQueue.signal()
	else:
		leaders++
		mutex.signal()
		leaderQueue.wait()
	doSomething()
	randevu.wait()
	mutex.signal()
	
def followerStatment():
	mutex.wait()
	if leaders>0:
		leaders--
		leaderQueue.signal()
	else:
		followers++
		mutex.signal()
		followerQueue.wait()
	doSomething()
	randevu.signal()