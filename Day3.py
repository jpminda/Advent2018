import numpy as np
import re
size = 1000
import matplotlib.pyplot as plt

claims = np.zeros(shape=(size,size))
tempclaims = np.zeros(shape=(size,size))

#part 1
f = open('day3input.txt')
for line in f:
	ID,startX,startY,sizeX,sizeY = map(int, re.findall(r'\d+', line))
	claims[startX:startX + sizeX, startY:startY + sizeY] = claims[startX:startX + sizeX, startY:startY + sizeY] + 1

#after filling the array with "1s", just take sum of anything that is 2 or more
final = sum(sum(claims>=2))
print(final) #part 1 final Answer

#day 2
#open the file again and run though as before.
f = open('day3input.txt')
for line in f:
	ID,startX,startY,sizeX,sizeY = map(int, re.findall(r'\d+', line))
	tempclaims[startX:startX + sizeX, startY:startY + sizeY] = 1
	#for each claim, check to see if all of the sqaures match 1 and onlt one previous claim
	#that means that a claim was filed only once
	if (tempclaims[startX:startX + sizeX, startY:startY + sizeY] == claims[startX:startX + sizeX, startY:startY + sizeY]).all():
		unique = ID #that's the unique ID
		claims[startX:startX + sizeX, startY:startY + sizeY] = 10 #this will hilight it on the map

	tempclaims[startX:startX + sizeX, startY:startY + sizeY] = 0


print(unique) #the answer
plot the map
plt.imshow(claims)
plt.show()




