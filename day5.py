#test example
#polymer = str('dabAcCaCBAcCcaDA')
filename = ('day5input.txt')
with open(filename, 'r') as f:
    polymer = f.read()#.splitlines()

matches = True

while matches == True:	
	matches = False
	i = 0
	#print(polymer[i],polymer[i+1])
	#if polymer[i].islower() ==  polymer[i+1].isupper():
	while i < (len(polymer) - 1):
		if polymer[i] ==  polymer[i + 1].swapcase():
			matches = True
			new_polymer = polymer.replace(polymer[i] + polymer[i + 1], '', 1)
			polymer = new_polymer
		else:	
			i = i + 1

print(polymer)
print(len(polymer))
