#opens a file, reads and spilts the lines, getting rid of the \n
from collections import Counter
with open('day2.txt') as f:
    d = f.read().splitlines()
size = len(d)
sum2 = 0
sum3 = 0
this = set()

for i in range(size):
	this.clear()
	cs = (Counter(d[i]))
	for k,v in cs.items():
		this.add(v) 
	print(this)
	if 2 in this:
		sum2 = sum2 + 1
	if 3 in this:
		sum3 = sum3 + 1
cs = sum2 * sum3

print(cs) #final answer
