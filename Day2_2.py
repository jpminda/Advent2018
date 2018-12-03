#Advent of Code, Day 2 part 2
#jpminda, Dec 2. 2018
with open('day2.txt') as f:
    d = f.read().splitlines()

#caculate the size of the string
size = len(d)
#set the mismatches at 0.
#we're ooking for the two strings that differ by only one letter
mis_match = 0

#nested loops to compare eveything with everything
for i in range(size):
	for j in range(size):
		#zero this for each string comparison
		mis_match = 0
		#these are the two strings you are going to compare
		dd = (d[i])
		ee = (d[j])
		#as lomg as you are not going to compare the string to itself
		if i != j:
			#loop though all the letter
			for k in range(len(dd)):
				if dd[k] != ee[k]:
					#add up all the mismatches
					mis_match = mis_match + 1
		#if the total mismatches = 1, the you've found the pair.
		#store the number (the index) for that string so you can refer to it later
		#and store the index for the mismatched letter
		if mis_match == 1:
			final_1 = d[i]
			final_2 = d[j]
			for k in range(len(dd)):
				if final_1[k] != final_2[k]:
					remove = k
#print the two strings					
print(final_1)
print(final_2)
#print the letter you need to remove
print(final_2[remove])
#print the string up to that letter then skip over it and print the rest
print(final_1[0:remove] + final_1[remove+1:size]) #this is the final string



