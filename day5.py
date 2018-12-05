#test example
#filename = ('day5inputE.txt')

filename = ('day5input.txt')
with open(filename, 'r') as f:
    orig_polymer = f.read()

new_polymer = orig_polymer

matches = True


while matches == True:	
	matches = False
	i = 0
	#print(polymer[i],polymer[i+1])
	#if polymer[i].islower() ==  polymer[i+1].isupper():
	while i < (len(new_polymer) - 1):
		if new_polymer[i] ==  new_polymer[i + 1].swapcase():
			matches = True
			new_polymer = new_polymer.replace(new_polymer[i] + new_polymer[i + 1], '', 1)
			#polymer = new_polymer
		else:	
			i = i + 1

#correct answer for part 1
print(len(new_polymer)) 

#part 2
polymer_size = []
for i in range(25):
	new_polymer = orig_polymer
	s = chr(i + 65)
	new_polymer = new_polymer.replace(s, '')
	S = chr(i + 97)
	new_polymer = new_polymer.replace(S, '')
	matches = True
	while matches == True:	
		matches = False
		i = 0
		while i < (len(new_polymer) - 1):
			if new_polymer[i] ==  new_polymer[i + 1].swapcase():
				matches = True
				new_polymer = new_polymer.replace(new_polymer[i] + new_polymer[i + 1], '', 1)
				#polymer = new_polymer
			else:	
				i = i + 1



	polymer_size.append(len(new_polymer))
polymer_size.sort()
#correct Answer for part 2
print(polymer_size[0]) 



