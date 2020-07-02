# Python was the sixth most popular programming language in 2010 on StackOverflow (left image). It continually went
# up in the ranks to being the most popular among all in 2018 (right image).

# you can also give multiple arguments in function

def area(a, b):
    return a * b


print("area is:", area(4, 5))


# you can also give multiple arguments without defining in function

def mean(*args):
    my_mean = sum(args) / len(args)
    return my_mean


print(mean(1, 2, 5))
