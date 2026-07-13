name="yashvi jivrajani"
print(name[0:6])

namelen=len(name)
print(namelen)
print(len(name))

print(name[:6])

print(name[3:])

print(name[:-3])
# does not consider last 3 letters. python does length of string-3
# 16-1 is 15 and 16-3 is 13 but 15:13 is not possible as reverse string

print(name[-3:-1])
# here 13:15 is possible

nm="harry"
print(nm[-4:-2])

print(name.upper())
# upper case

print(name.lower())
# lower case
# strings are immutable in python. you can't change them but you can make a new one
# here name is a string but name.upper is a different string with upper case letters

print(nm.rstrip("y"))
print(nm.rstrip("h"))
# removes a particular character. it can not remove from front

print(name.replace("jivrajani","yashvi"))
# replaces a particular string with another string

print(name.split(" "))
# splits the string into a list of strings based on the separator provided.
# here it splits the name into first name and last name based on the space character

print(name.capitalize())
# first letter capitala nd the rest are made small

print(name.title())
# first letter of each word is capitalized and the rest are made small

print(name.count("i"))
# counts the number of occurrences of a particular character in the string

print(name.find("j"))
# returns index of first occurence
# if not found returns -1

print(name.endswith("ani"))
# returns true if string ends with the specified suffix, otherwise returns false

print(name.endswith("hv",3,5))
# can also check for a specific position

print(name.isalnum())
# returns true if string only contains letters and number, otherwise returns false(spaces and special characters)
# isalpha() returns true if string only contains letters

print(name.islower())
# returns true if all characters are lower
# isupper() returns true if all characters are upper

print(name.swapcase())
# lowercase to uppercase and vice versa

