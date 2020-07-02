# making a programme
def statements(phrase):
    interrogatives = ("how", "why", "what")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


result = []
while True:
    user_input = input("enter your statement:")
    if user_input =="\end":
        break
    else:
        result.append(statements(user_input))
print("  ".join(result))

# you can also used list comprehension too
#if you want to print only int values
temp=[10,10.4,50,99,5.2]
new_temp=[i for i in temp if type(i)==int]
print(new_temp)

#if you want to replace anydata then
temp=[10.1,"anu",56,85]
new_temp=[i if type(i)==int else 0 for i in temp]
print(new_temp)