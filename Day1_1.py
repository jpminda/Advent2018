import numpy as np
data = np.loadtxt("input.txt")

#challenge 1_1
finalFreq = sum(data)
print(finalFreq)

#challenge 1_2
size = len(data)
match = False
freq = 0
freqList = [freq]

while match == False:
	for i in range(size):
 		freq = freq + data[i]
 		if freq in freqList:
 			firstRepeat = freq
 			match = True
 			break #this is weak, but otherwise it completes the whole loop. 
 				#I'm sure there's a better way, 
 		freqList.append(freq)

print(firstRepeat)
 			