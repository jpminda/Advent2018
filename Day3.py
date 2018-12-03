import numpy 
#import matplotlib.pyplot as plt
#claims = numpy.loadtxt('day3input.txt')





with open('day3inputE.txt') as f:
	claims=f.read()
	while '#' in claims:
		claims=claims.replace('#', '')
	while ' @ ' in claims:
		claims=claims.replace(' @ ', '')
	while ':' in claims:
		claims=claims.replace(':', '')
	while ',' in claims:
		claims=claims.replace(',', '')
	while 'x' in claims:
		claims=claims.replace('x', '')
	while ' ' in claims:
		claims=claims.replace(' ', '')




#print(claims)

#claims = list(claims)
#print(claims)

#claims = numpy.array(claims)
print(claims)

print(claims[0:12])
