
def mytuple(tuple):
    lst = list(tuple)
    print(lst)
    key_lst, value_lst = [],[]
    for i in range(len(lst)):
        if i % 2 == 0:
            key_lst.append(lst[i])
        else:
            value_lst.append(lst[i])

    return dict(zip(key_lst,value_lst))



test = (2, "Python", (3, 5), [2, "Python", (3, 5)], "Maktab")


my_tuple = mytuple(test)
print(my_tuple)

