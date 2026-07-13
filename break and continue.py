for i in range(12):
    print("5 x",i+1,"=",5*(i+1))

for i in range(12):
    if i==10:
        break
    if i==5:
        continue
    print("5 x",i+1,"=",5*(i+1))

for i in range(12):
    print("5 x",i+1,"=",5*(i+1))
    if i==10:
        break
    if i==5:
        continue

j=0
while True:
    print(j)
    j=j+1
    if(j%10==0):
        break

# pass is used to tell python to not to do anything, it is used as a placeholder
for i in range(10):
    if i%2==0:
        pass
    else:
        print(i)