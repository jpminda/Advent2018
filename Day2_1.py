#opens a file, reads and spilts the lines, getting rid of the \n
from collections import Counter
with open('day2.txt') as f:
    d = f.read().splitlines()

size = len(d)
sum2 = 0
sum3 = 0
this = set() # I leared about sets, which are really useful

#loop Through everything
for i in range(size):
	this.clear()
	#counter will tally up how many of something there are
	#put that into cs, which is now a container of counts for how may times each letter appears
	cs = (Counter(d[i]))
	#k is the letter, and V is the count
	for k,v in cs.items():
		this.add(v) 
	#now we just look for counts of 2 and 3 and add them up	
	if 2 in this:
		sum2 = sum2 + 1
	if 3 in this:
		sum3 = sum3 + 1
#multiply, since that is the main task

cs = sum2 * sum3
print(cs) #final answer
