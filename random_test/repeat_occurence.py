a = []
n = int(input("enter the element in list: "))
for x in range(n):
    element = int(input("enter the element" + str(x+1) + ":" ))
    a.append(element)
print(a)
c = []
count = 0
b = input("enter the word to remove")
n = int(input("enter the occurrence to remove"))
for i in a:
    if (i == b):
        count = count + 1
        if (count!=n):
            c.append(i)
        else:
            c.append(i)
    if (count == 0):
        print("item not found")
    else:
        print(count)
        print("updated list",c)
        print(set(a)) 