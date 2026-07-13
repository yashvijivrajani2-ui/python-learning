import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)

if timestamp<"12":
    print("good morning sir")

elif timestamp<"16":
    print("good afternoon sir")

else:
    print("good evening sir")

# else:
#     print("good night sir")