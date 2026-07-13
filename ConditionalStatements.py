a=int(input("enter your age:"))
print("your age is:",a)
if a>18:
    print("you are eligible to vote")

elif a==18:
    print("you can vote after getting voting card")

else:
    print("you are not eligible to vote")
print("thank you")

# nested if
b=int(input("enter your marks:"))
print("your marks are:",b)
if b>=90:
    print("A grade")
elif b>=80:
    print("B grade")
elif b>=70:
    print("c grade")
else:
    print("fail")

