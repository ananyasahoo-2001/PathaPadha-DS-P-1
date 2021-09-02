# To add "ing" at the end of a string or add "ly" if the string already ends with "ing" for a string whose length is atleast 3

s = input("Enter a string : ")

if len(s) >= 3:
    if s[-3:] == "ing":
        s = s + "ly"
        print(s)
    else:
        s = s + "ing"
        print(s)
else:
    print("The length of string is less than 3")
    
        
