# Osama M. Afifi osama.egt@gmail.com -  27/Nov/2014
#
# The Dining Philosophers Problem solved using Multiplex
#
# The Classic dining philosophers problem solved using a multiplex initialized with n-1 to avoid deadlocks
# Starvation though can occur in this solution frequently by making a philosopher starve and switching between the others
# ex : Philosopher 0 waits and 1 and 3 eat then they put down their forks and 2 and 4 eat and so on which make philosopher 0 starve without eating
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

 multiplex = Sempahore(n-1) #initialize a multiplex allowing n-1 threads to get their forks leaving one thread to avoid Deadlock
 
def get_forks(i):
	multiplex.wait()
	fork[right(i)].wait()
	fork[left(i)].wait()

def put_forks(i):
	fork[right(i)].signal()
	fork[left(i)].signal()
	multiplex.signal()