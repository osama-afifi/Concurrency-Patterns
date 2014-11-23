# Osama M. Afifi osama.egt@gmail.com -  24/Nov/2014
#
# Producer Consumer Concurrency Pattern
#
# We have a producer which produces some kind of object and adds it to a buffer and a consumer which consume this object
# Accessing the buffer should be exclusive
# This technique is used in even handling where producers wait for events and consumers are called event handlers
# This code is deadlock free if you can see anything else feel free to tell me

mutex = Sempahore(1)
items = Semaphore(0)

def Producer:
	while True:
		event = waitForEvent()
		mutex.wait()
		buffer.add(event)
		mutex.signal
		items.signal()

def Consumer:
	while True:
		items.wait()
		mutex.wait()
		event = buffer.get()
		mutex.signal()
		event.process();
		