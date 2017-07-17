from math import sqrt
j = 2
while j < 100:
	i = 2
	k = sqrt(j)
	while (i <= k):
		if j % i == 0:
			break
		i = i + 1
	if (i > k):
		print j
	j = j + 1

def isprime(x):
	if x == 1:
		return False
	k = int(sqrt(x))
	for i in range(2, k+1 ):
		if x%i== 0:
			return False
	return True

for j in range(2, 101):
	if isprime(j):
		print j