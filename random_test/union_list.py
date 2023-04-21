a = [1,2,3,4,5]
b = [6,7,8,9,0]
# print(a+b)  ## union of list
# print(list(set().union(a,b)))
a.extend(b)
print(a)