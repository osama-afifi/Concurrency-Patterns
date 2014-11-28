# Osama M. Afifi osama.egt@gmail.com -  25/Nov/2014
#
# Writer-Priority Reader Writer Concurrency Pattern
#
# A Multiple Reader Single Writer exclusive access used on databases, file-systems and many other datastructures.
# This Version ensures that the Writer has a priority over reader
# Most Threading libraries have priority mechanism which makes this easier (giving writer high priority in context switching)
# This code is deadlock free if you can see anything else feel free to tell me.









# Did not list the code because I  found the Operating System threading priority mechanisms easier to implement
# Maybe you could send me your suggestions on osama.egt@gmail.com
	
		