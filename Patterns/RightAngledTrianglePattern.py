input = int(input("Enter the number"))

#-------------
# Star Pyramid
for i in range(0, input+1):
    print(i*"* ")
    
#---------------
# Number Pyramid
counterStr = ""
for i in range(0, input+1):
    counterStr += str(i+1)
    print(counterStr)

#--------------------
# Number Pyramid - II
for i in range(0, input+1):
    print(f"{i}"*i)
    
#-----------------------
# Inverted Right Pyramid
for i in range(0, input+1):
    print("* " * (input - i))
