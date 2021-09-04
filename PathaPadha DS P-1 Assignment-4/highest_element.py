# To find the highest element in a list

# Method-1

l = [15, 43, 20, 32, 62, 13]
l.sort()

highest_elem = l[-1]
print("Highest element in the list : " , highest_elem)




#Method-2

l = [15, 43, 20, 32, 62, 13]
highest_elem = l[0]

for i in l:
    if i > highest_elem:
        highest_elem = i
print("Highest element in the list : " , highest_elem)


