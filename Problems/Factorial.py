def factorial(value):
    if(type(value) == int):
        if(value == 0):
            return 1
        else:
            return (value * factorial(value - 1))
    else:
        return -1

# factorial("sdfgh")
print(factorial(10))