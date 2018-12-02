from collections import Counter
with open('day2.txt') as f:
    d = f.read().splitlines()


size = len(d)
match = 0

for i in range(size):
	match = 0
	dd = list(d[i])
	for j in range(len(dd)):
		if dd[j] == dd[j]:
			match = match + 1
print(match)