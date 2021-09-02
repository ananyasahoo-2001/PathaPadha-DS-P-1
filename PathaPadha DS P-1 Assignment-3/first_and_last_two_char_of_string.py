# To get a string made of first two and last two characters from a given string

s = input("Enter a string : ")

if (len(s) >= 2):
    new_str = s[0:2] + s[-2:]
    print(new_str)
else:
    print("Empty string")
