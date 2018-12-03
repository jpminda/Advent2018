import numpy as np
data = np.loadtxt("input.txt")

#challenge 1_1
print(sum(data))

#challenge 1_2
size = len(data) #the size of the list of changes
freq_set = set() #a set to store the list of freq. Sets store unique numbers so as soon as a number is 
i = 0
freq = 0
while ((freq in freq_set)==False):
	freq_set.add(freq)
	freq = freq + data[i]
	i = (i + 1) % size
print(freq)
