def printNumbers(n):
	if (n==0):
		return 0
	printNumbers(n-1)
	print(n)

printNumbers(10)