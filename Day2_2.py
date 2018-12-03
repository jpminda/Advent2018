with open('day2.txt') as f:
    d = f.read().splitlines()

size = len(d)
mis_match = 0

for i in range(size):
	for j in range(size):
		mis_match = 0
		dd = list(d[i])
		ee = list(d[j])
		if i != j:
			#print (i,j)
			for k in range(len(dd)):
				if dd[k] != ee[k]:
					#print(j)
					mis_match = mis_match + 1
		if mis_match == 1:
			final_1 = d[i]
			final_2 = d[j]
			for k in range(len(dd)):
				if final_1[k] != final_2[k]:
					print(k)
					remove = k
					
print(final_1)
print(final_2)
print(final_2[20])
print(final_1[0:remove] + final_1[remove+1:size]) #this is the final string



