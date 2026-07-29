# basic of list
marks=[94.4, 88.5, 76.3, 92.1, 85.0]
print("Marks:", marks)
print(len(marks))
print(marks[0])
print(marks[1])

# basic of list in multi category data
student=['karan',85,'delhi',99.5]
print("Student:", student)
print(len(student))
student[0]='arjun'
print("Student:", student)

# list slicing
print(marks[1:3])

# list methods
list=[1,2,3,4,5]
print(list)
#append
list.append(6)
print(list)
#descending order
list.sort(reverse=True)
print(list)
# reversing the list
list.reverse()
print(list)
#remove element
list.remove(3)
print(list)
#insert element(index, value)
list.insert(0, 2)
print(list)
# pop from end
list.pop()
print(list)
# pop from index
list.pop(0)
print(list)

# basic of tuple
tup=(1,2,3,4,5)
print(type(tup))
print(tup[0])
# tuple of single element still needs a comma
tup1=(1,)
print(type(tup1))
print(tup1)

# tuple slicing
print(tup[1:3])

# tuple methods
# counts total occurences
print(tup.count(3))
# returns the index of first occurence
print(tup.index(4))

# excercise
# 1. WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
# mov1=input("Enter your first favorite movie: ")
# mov2=input("Enter your second favorite movie: ")    
# mov3=input("Enter your third favorite movie: ")
# movies=[mov1, mov2, mov3]
# print(movies)

# # another way
# movies1=[]
# movies1.append(input("Enter your first favorite movie: "))
# movies1.append(input("Enter your second favorite movie: "))
# movies1.append(input("Enter your third favorite movie: "))
# print(movies1)

# 2. WAP to check whether a given list is palindrome or not
a=[1,2,3,2,1]
print(a)
b=a.copy()
b.reverse()
if (a==b):
    print("The list is palindrome")
else:
    print("The list is not palindrome")

c=[1,2,3]
print(c)
d=c.copy()
d.reverse()
if (c==d):
    print("The list is palindrome")
else:
    print("The list is not palindrome")

# 3. WAP to count the number of occurrences of element "A" in a list and also sort them
l1=["C","D","A","A","B","B","C"]
print("no. of occurrences of A:", l1.count("A"))

l1.sort()
print("sorted grades are:",l1)