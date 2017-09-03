##############################
#           max3.py          #
#  The max out of three ints #
#       By Isaac Bankier     #
##############################

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if num1 > num2 and num1 > num3: # if num1 is biggest
    print(num1)

elif num2 > num1 and num2 > num3:  # if num2 is biggest
    print(num2)

elif num3 > num1 and num3 > num2:  # if num3 is biggest
    print(num3)

elif num1 == num2 == num3:  # if equal
    print(num1)
