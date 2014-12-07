# Osama M. Afifi osama.egt@gmail.com -  07/Nov/2014
#
# Cigarette Smokers Problem Solution
#
# Three Smokers and one Agent, the Agent pulls out one of the three ingredients of a cigarette (Tobacco, Paper or Match)
# while each of the smokers hold only one ingredient different than each other
# 1st Smoker has Tobacco
# 2nd Smoker has Papers
# 3rd Smoker has Matches
# It resembles an Operating System (Agent) and User processes (smokers) where the compete on system resources (cigarette ingredients).
# This code is deadlock free if you can see anything else feel free to tell me.

mutex = Semaphore(1)
tobaccoSmoker = Semaphore(1)
paperSmoker = Semaphore(1)
matchSmoker = Semaphore(1)
tobaccoOnTable = 0
paperOnTable = 0
matchOnTable = 0


# Agent has three different pushers he uses to assign smokers
# Pusher A pushes tobacco onto the Table
def PusherA:
	mutex.wait()
	if paperOnTable:
		paperOnTable -= 1
		matchSmoker.signal()
	elif matchOnTable:
		matchOnTable -= 1
		paperSmoker.signal()
	else:
		tobaccoOnTable += 1
	mutex.signal()
	

# Pusher B pushes paper onto the Table
def PusherB:
	mutex.wait()
	if tobaccoOnTable:
		tobaccoOnTable -= 1
		matchSmoker.signal()
	elif matchOnTable:
		matchOnTable -= 1
		tobaccoSmoker.signal()
	else:
		paperOnTable += 1
	mutex.signal()
	

# Pusher C pushes matches onto the Table
def PusherC:
	mutex.wait()
	if tobaccoOnTable:
		tobaccoOnTable -= 1
		paperSmoker.signal()
	elif paperOnTable:
		paperOnTable -= 1
		tobaccoSmoker.signal()
	else:
		matchOnTable += 1
	mutex.signal()

# Smoker with Tobacco
def TobaccoHoldingSmoker():
	tobaccoSmoker.wait()
	makeCigarettes()
	smoke()

def PaperHoldingSmoker():
	paperSmoker.wait()
	makeCigarettes()
	smoke()

def MatchHoldingSmoker():
	matchSmoker.wait()
	makeCigarettes()
	smoke()
	
	
def makeCigarettes():
	pass

def smoke():
	pass


	
	