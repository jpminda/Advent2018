import numpy as np
data = np.loadtxt("input.txt")
freq = 0
size = len(data)

#challenge 1_1
for i in size:
	freq = freq + data[i]
print(freq)

#challenge 1_2
freq = 0
for i in size:
	freq = freq + data[i]
	fregList.append(freq)

	for j in len(freqList):
		if freqList[j] == freq: 

