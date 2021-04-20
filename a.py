def f2048(power):
	result = 0
	for i in range(2, power+1):
		result = 2*result + 2**i
	return result

for i in range(1,20):
	print str(2**i)+" \t : "+str(f2048(i))
