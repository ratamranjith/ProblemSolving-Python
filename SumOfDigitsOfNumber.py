def sum_of_digits(n):
	if(n == 0):
		return n
	return (n%10) + int(sum_of_digits(n/10))
print (sum_of_digits(42304))