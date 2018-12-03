import numpy as np
import re
size = 2000
#import matplotlib.pyplot as plt
claims = np.zeros(shape=(size,size))
print(claims)
f = open('day3input.txt')
for line in f:
	ID,startX,startY,sizeX,sizeY = map(int, re.findall(r'\d+', line))
	claims[startX:startX + sizeX, startY:startY + sizeY] = claims[startX:startX + sizeX, startY:startY + sizeY]+1
print(ID)
print(startX)
print(startY)
print(sizeX)
print(sizeY)
print(claims)
final = sum(sum(claims>=2))
print(final)