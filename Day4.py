import re
import numpy as np

filename = 'day4inputE.txt'

#part 1

d = [line.strip('\n') for line in open(filename,"r")]
d.sort()



for i in range(len(d)):
	time,function = d[i].split("]")
	yyyy,mm,dd,hh,mm = re.findall(r'\d+', time)
	gid = re.findall(r'\d+', function)
	print(gid)
	if 'begins' in function:
		awake = True
	if 'wakes' in function:
		awake = True
	if "asleep" in function:
		awake = False
	stats = {"Gaurd" : gid}

print(stats)













#for line in f:
#	ID,startX,startY,sizeX,sizeY = map(int, re.findall(r'\d+', line))
#	claims[startX:startX +