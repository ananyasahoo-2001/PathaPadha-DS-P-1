# To sort a list without using sort()

lst = [12, 45, 10, 23, 72, 7 ]
new_lst = []

while lst:
    small = lst[0]
    for i in lst:
        if i < small:
            small = i
    new_lst.append(small)
    lst.remove(small)

print("Sorted list is : " , new_lst)
