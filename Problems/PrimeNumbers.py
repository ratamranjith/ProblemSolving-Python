n = 1
retVal = [i for i in range(1, n) if all(i%k for k in range(3, i))]
print(retVal)
