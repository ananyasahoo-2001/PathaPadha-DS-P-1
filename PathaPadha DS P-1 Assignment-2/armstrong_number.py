# To find whether a number is Armstrong number or not

num = int(input("Enter a number : "))
total = 0
n = num

while n > 0:
    c = n % 10
    total = total + c**3
    n = n // 10

if total == num:
    print(num , " is an Armstrong number")
else:
    print(num , " is not an Armstrong number")

