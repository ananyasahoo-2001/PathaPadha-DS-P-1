# Python function that takes a list as argument and returns a new list with unique elements of the first list

def unique(l):
    new_lst = []
    for i in l:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


lst = [2, 3, 4, 3, 3, 5, 5, 9, 6, 9]
print(unique(lst))

