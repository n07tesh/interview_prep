def find_odd_occurring(alist):
    ans = 0
    for ele in alist:
        ans ^= ele
    return ans


n = int(input("enter the length of list"))
alist = []
for i in range(1,n):
    input_ = int(input("enter the number of list"))
    alist.append(input_)
lis = find_odd_occurring(alist)
print(lis)

