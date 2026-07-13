a=input("Enter your name")
print("my name is",a)

x=input("enter first number")
y=input("enter second number")
print(x+y)
# gives string sumation

print(int(x)+int(y))
# gives numeric sumation

#  string can use both "" and ''
name='yashvi'
print(name)

# string
print("he said \"he wants to eat an apple\"")
print('he said "he wants to eat an apple"')
# both are same

# multi string
apple='''Hi Yashvi
I want to eat an apple'''
print(apple)
print(name[0])

# using for print all letters of the name
print("let's use a for loop")
for character in name:
    print(character)