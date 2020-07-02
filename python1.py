# integer value sum will be
x = 10
y = 20
sum1 = x + y
print("result after adding two integer values:", sum1)
# sum of two string will value will be basically the concatenation of two strings
u = "10"
v = "20"
# you can also use single quotes for defining any string value too
sum2 = u + v
print("concatenation of two string values will be:", sum2)
# you can also print the type of each and every value
print("types of all the values used in the above code is:", type(x), type(y), type(u), type(v))
# you can also store multiple values in a single variable using list
my_list = [9.1, 5.6, 3.2]
print("my list is:", my_list)
# list in python is of hetrogenous nature that means you can store multiple types of values in a single list
# basically you can check all the methods applied on list too by using dir function
my_sum = sum(my_list)
my_len = len(my_list)
my_mean = my_sum / my_len
print("the average value or the mean of the list is:", my_mean)
