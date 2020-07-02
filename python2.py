# calculating the maximum value from the list by using the built in function

my_list = [9.1, 5.2, 10.1, 11.2, 10.1]
print("my list is:", my_list)
max_value = max(my_list)
print("the maximum value from the list is:", max_value)
# you can also append the value in the list or remove the value from the list

my_list.append(6)
print("my new list after appending looks like:", my_list)
my_list.remove(5.2)
print("my new list after removing the particular value from the list is:", my_list)

# calculating the occurrences of the similar value in the list by using the built in method
num = my_list.count(10.1)
print("number of occurrences is of 10.1 in the list :", num)

# Did you know that Python was first released in 1991? Python 2 was released in 2000, and Python 3 (the current
# version) in 2008.

# you can also make dictionary too
my_dict = {"anu": 9.6, "aloo": 9.2, "ansh": 10}
print("my dictionary looks like:", my_dict)
# you can print values and keys from dictionary too
print("values of my dict is:", my_dict.values())
print("keys of my dict is:", my_dict.keys())

# you can also create tuple too
my_tuple = (9, 8, 7)
print("my tuple looks like:", my_tuple)
