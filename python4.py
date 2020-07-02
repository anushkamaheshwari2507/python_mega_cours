# you can make your own function too


def mean(my_list):
    my_mean = sum(my_list) / len(my_list)
    return my_mean


print("mean of the list by using my own function")
print(mean([10, 12, 5, 6, 8, 4]))


# you can calculate the area of a square using your own function

def area(s):
    my_area = s * s
    return my_area


print("area of the square is:")
print(area(4))


# you can take input from user directly and also apply conditionals too

def temperature(temp):
    if temp > 7:
        return "warmer"
    else:
        return "colder"


user_input = int(input("enter the value:"))
print(temperature(user_input))

# you can also do string formatting too

user_input = input("enter your name:")
message = "Hello %s!" % user_input
print(message)

# you can also use multiple values during string formatting like

user_input = input("enter your name:")
user_surname = input("enter your surname:")
message = "Hello %s %s!" % (user_input, user_surname)
print(message)
