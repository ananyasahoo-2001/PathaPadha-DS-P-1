# Python function to take list as argument and return the sum of all the numbers in a list


def add(l):
    total = 0
    for i in l:
        total = total + i
    return total


lst = [10, 15, 28, 34, 45, 68]
print(add(lst))

