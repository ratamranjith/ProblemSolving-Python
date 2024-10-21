def rotate(arrayValue, steps):
	length   = len(arrayValue)
	original = []
	temp     = []
	print(arrayValue[length - steps:] + arrayValue[0:length-steps])
		


rotate([10,2,3,4,5,6], 3)