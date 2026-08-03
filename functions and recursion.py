def sum(a,b):
    s=a+b
    return s

print(sum(5,6))

def my_function():
    print("hello from a function")

my_function()

def name(fname):
    print(fname + "jivrajani")

name("yashvi ")

# factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

# recursion
# print n to 1 in reverse order
def show(n):
    if(n==0):
        return 0
    else:
        print(n)
        show(n-1)
show(5)

