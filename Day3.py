import numpy as np
import re
size = 1000
import matplotlib.pyplot as plt
claims = np.zeros(shape=(size,size))
tempclaims = np.zeros(shape=(size,size))
f = open('day3input.txt')
for line in f:
	ID,startX,startY,sizeX,sizeY = map(int, re.findall(r'\d+', line))
	tempclaims[startX:startX + sizeX, startY:startY + sizeY] = 1
	if tempclaims.any()!=claims.any():
		print(ID)
	claims[startX:startX + sizeX, startY:startY + sizeY] = claims[startX:startX + sizeX, startY:startY + sizeY]+ tempclaims[startX:startX + sizeX, startY:startY + sizeY]
	if tempclaims.any()!=claims.all():
		print(ID)
print(claims)
final = sum(sum(claims>=2))
print(final)
plt.imshow(claims)
plt.show()




