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
		for j in range(i-1):
			if freqList[i] == freqList[j]:
				firstRepeat = freqList[j]
				match = True

print(freqList)
print(match)

print(firstRepeat)

		

		



		




