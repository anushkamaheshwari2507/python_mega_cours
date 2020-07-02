# if you want to read any file or to read the data of many file
my_file = open("furit.txt")
# if you want to read whole data of any file
print(my_file.read())
# you can also close the file after opening but it is not mandatory to close it
content = my_file.read()
my_file.close()
print(content)
# you can also use with keyword just to open a file
with open("furit.txt")as my_file:
    content = my_file.read()
print(content)
# to write something in the file you have to use w as an attribute with open statement
with open("vegetable.txt", "w")as myfile:
    myfile.write("tomato\nonion\ncarrot\ngarlic")
# you can also append the file by using attribute a
with open("vegetable.txt", "a+")as my_file:
    my_file.write("\nanushka")
