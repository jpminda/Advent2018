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
 			match = True
 			firstRepeat = freq
 		freqList.append(freq)

#print(freqList)
print(match)
 			