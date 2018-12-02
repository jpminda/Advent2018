from collections import Counter
with open('day2.txt') as f:
    d = f.read().splitlines()


size = len(d)
match = 0

#loop though all the exemplars
#for each exeamplars i comparare to all the exemaplrs except itself
#if theere is a mismatch, count how many
#then if you get a count of 1, record those two values.
#then remove any non matching letters
#that is the answer 

for i in range(size):
	match = 0
	dd = list(d[i])
	for j in range(len(dd)):
		if dd[j] == dd[j]:
			match = match + 1
print(match)