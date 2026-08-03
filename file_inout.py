# f=open("sample.txt", "r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# f=open("sample.txt", "w")
# f.write("this is a new line")
# f.close()

# f=open("sample.txt", "a")
# f.write("\nthis is done with append")
# f.close()

# f=open("sample.txt", "r+")
# f.write("abc")
# f.close()

# r+ read+overwrite pointer is at start no truncate
# w+ write+overwrite pointer is at start truncate
# a+ read+append pointer is at end no truncate

# with open("sample.txt","r") as f:
#     data=f.read()
#     print(data)

# import os
# os.remove("sample.txt")

with open("practice.txt","w") as f:
    f.write("hello everyone!\ni like python programming\nthis is a new line wiith java")
    f.close()

with open("practice.txt","r") as f:
    data=f.read()

new=data.replace("java","python")
print(new)

if(data.find("like")):
    print("yes it is there")
else:
    print("no it is not there")