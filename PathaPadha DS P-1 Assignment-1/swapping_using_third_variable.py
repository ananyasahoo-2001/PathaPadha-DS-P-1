# Swapping two numbers by using third variable

num_1 = int(input("Enter the first number : "))
num_2 = int(input("Enter the second number : "))

print("Before swapping : \n1st number : " , num_1 , "\n2nd number : " , num_2)

var = num_1
num_1 = num_2
num_2 = var

print("After swapping : \n1st number : " , num_1 , "\n2nd number : " , num_2)
