def print_numbers(value, order = 'asc'):
	if(value != 0):
		print("Order: ", order)
		if(order == 'des'):
			print(value)
			print_numbers(value - 1, order)
		else:
			print_numbers(value - 1, order)
			print(value)
	else:
		return

print_numbers(10, 'asc')