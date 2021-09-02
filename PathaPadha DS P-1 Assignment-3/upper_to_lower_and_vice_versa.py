# To convert the characters which are in lowercase to uppercase and viceversa and then display the updated string

s = input("Enter a string : ")
new_str = ""

for i in s:
    if (i.isupper()):
        c = i.lower()
        new_str = new_str + c
    elif (i.islower()):
        c = i.upper()
        new_str = new_str + c
print(new_str)
