# Osama M. Afifi osama.egt@gmail.com -  27/Nov/2014
#
# The Dining Philosophers Problem solved using alternating lefties and righties
#
# This solution make odd positioned philosophers righties and even positioned lefties
# This guarantees no deadlock and make the solution as fair as possible with maximum philosophers even
# The Solution is completely fair with even number of philosophers but is slightly unfair when the number is odd where to righties sit next to each other (1st and last)
# This code is deadlock free if you can see anything else feel free to tell me.


n = 5 # for standard Dining Philosophers problem
forks = [Semaphore(1) for i in range(n)]



def dining_philosphers():
	while True:
		think()
		get_forks()
		eat()
		put_forks()

# do something useful in the following two functions
def think():
	pass
def eat(): 
	pass		
		
def left(i): 
	return i
	
def right(i):
 return (i + 1) % n


def get_forks(i):
	if i%2==0:
		fork[right(i)].wait()
		fork[left(i)].wait()
	else:
		fork[left(i)].wait()
		fork[right(i)].wait()
	

def put_forks(i):
	if i%2==0:
		fork[right(i)].signal()
		fork[left(i)].signal()
	else:
		fork[left(i)].signal()
		fork[right(i)].signal()a