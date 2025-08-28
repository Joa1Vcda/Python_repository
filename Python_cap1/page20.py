"""methods in lists"""

# append-add a item from the end of list
# insert-add a element in the list(index,value)
# pop-deletes the end of the list or the chosen index
# del-deletes a chosen index
# clear-clear the list

list = [2, 4, 6, 8, 10, 11]
list.append(12)
print(list)
list.pop(-2)
print(list)
del list[-1]
print(list)
list.insert(0, 0)
print(list)
list.clear()
print(list)
