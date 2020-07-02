# you can also clear the whole list
my_list = [9, 8, 7, 6, 5]
my_list.clear()
print(my_list)

# you can also identify the index of any value from the list too because list has indexing in it
my_list = [9, 8, 7, 6, 5]
ii = my_list.index(7)
print("index value of 7 from the list is:", ii)

# if you want to get any item then just use built in method of the list
item = my_list.__getitem__(3)
print("printing the value present at the index 3 is:", item)

# slicing of the list is
print("partial values of the list is:", my_list[0:3])

# you can also do negative indexing too like
my_list = [9, 8, 7, 6, 5]
print("last two values of the list is:", my_list[-1])
