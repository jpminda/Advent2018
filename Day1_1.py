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
		freqList.append(freq)
		for j in range(i):
			if freqList[i] == freqList[j+1]:
				firstRepeat = freqList[j+1]
				match = True

print(freqList)
print(match)

print(firstRepeat)

		

		



		



