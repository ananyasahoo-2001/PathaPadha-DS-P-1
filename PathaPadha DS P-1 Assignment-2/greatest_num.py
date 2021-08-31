# To find the greatest number

num_1 = int(input("Enter the first number"))
num_2 = int(input("Enter the second number"))
num_3 = int(input("Enter the third number"))

if (num_1 < num_2 and num_1 < num_3):
    if num_2 < num_3:
        print("The greatest number is " , num_3)
    else:
        print("The greatest number is " , num_2)

if (num_2 < num_1 and num_2 < num_3):
    if num_1 < num_3:
        print("The greatest number is " , num_3)
    else:
        print("The greatest number is " , num_1)

if (num_3 < num_1 and num_3 < num_2):
    if num_1 < num_2:
        print("The greatest number is " , num_2)
    else:
        print("The greatest number is " , num_1)
