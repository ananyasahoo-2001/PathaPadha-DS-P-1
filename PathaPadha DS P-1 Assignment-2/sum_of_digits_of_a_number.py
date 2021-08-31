# To find the sum of digits of a number

num = int(input("Enter a number : "))
total = 0

while num > 0:
    c = num % 10
    total = total + c
    num = num // 10

print("The sum of digits of the number is " , total)
