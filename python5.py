# you can use for loops to print the list


def temperature(temp):
    for i in temp:
        print(i)


temperature([9.1, 5.2, 6.3])


# you can also print the round values too

def temperature(temp):
    for i in temp:
        print(round(i))


temperature([9.1, 5.2, 6.3])


# you can also apply conditional with loop

def values(value):
    for i in value:
        if type(i) == int and i > 5:
            print(i)


values([8, 4, 2, 6, 1, 5, 6.2])

# if you want to iterate over dictionary then
# you have to define whether you want to iterate over items,keys or values of dictionary
student_grades = {"anu": 9.6, "aloo": 9.2, "ansh": 10}

# when you want to iterate over items
for i in student_grades.items():
    print(i)

# when you want to iterate over keys
for i in student_grades.keys():
    print(i)

# when you want to iterate over values
for i in student_grades.values():
    print(i)

# you can also use while loop
user_name = input("enter the username")
while user_name == "pypy":
    user_name = input("Hello")
