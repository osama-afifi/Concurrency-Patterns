# Osama M. Afifi osama.egt@gmail.com -  28/Nov/2014
#
# The Dining Philosophers Problem solved using Tanenbaum's solution in his famous OS book
#
# This solution gives each philosopher different states between 1-thinking, 2-hungry and 3-eating 
# This guarantees no deadlock and make maximize the number of eating philosophers
# In this solution we deal woh philosophers states rather than forks semaphores (no forks semaphore array in this solution)
# Though starvation can still occur in Tanenbaum's solution
# This code is deadlock free if you can see anything else feel free to tell me.


n = 5 # for standard Dining Philosophers problem


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

 
 # State 1 for Thinking
 # State 2 for being Hungry
 # State 3 for eating
 philosopher_state = [1]*n # all begin at the thinking state
 ready_to_eat = [Semaphore(0) for i in range(n)]
 mutex = Semaphore(1)

def get_forks(i):
	mutex.wait()
	philosopher_state[i] = 2 # set the current philosopher to hungry state
	test(i)
	mutex.signal()
	ready_to_eat[i].wait() # will pass only if it's semaphore is signalled stating that it's ready to eat

def put_forks(i):
	mutex.wait()
	philosopher_state[i] = 1 # set the current philosopher back to thinking state
	test(left(i))
	test(right(i))
	mutex.signal()
		
def testPhilosopher(i):
	if philosopher_state[i] == 2 and # our current philosopher is hungry
	if philosopher_state[left(i)] != 3 and 
	if philosopher_state[right(i)] != 3 : # the adjacent philosophers are not eating (holding no forks i.e resources)
		philosopher_state = 3 # set the current philosopher as eating
		ready_to_eat[i].signal()
