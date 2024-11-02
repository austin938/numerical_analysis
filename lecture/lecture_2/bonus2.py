list = [1, 2, 2, 4]
for item in list:
    if item % 2 == 0:
        list.remove(item)
# print(list)

list = [1, 2, 2, 4]
list1 = [item for item in list if item % 2 != 0]
print(list1)