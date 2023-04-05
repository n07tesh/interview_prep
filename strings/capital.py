x = 'nitesh yadav'
y = x.split(' ')
temp = []
for i in y:
    temp.append(i.capitalize())
# print(temp)
new = ' '.join(temp)
print(new)