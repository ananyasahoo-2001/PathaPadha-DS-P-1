# To change a given string to a new string where the first and last chars have been exchanged

s = input("Enter a string : ")
new_str = s[-1] + s[1:-1] + s[0]
print(new_str)


