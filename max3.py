##############################
#           max3.py          #
#  The max out of three ints #
#       By Isaac Bankier     #
##############################

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if num1 > num2 and num1 > num3:
    print(num1)

elif num2 > num1 and num2 > num3:
    print(num2)

elif num3 > num1 and num3 > num2:
    print(num3)

elif num1 == num2 == num3:
    print(num1)
