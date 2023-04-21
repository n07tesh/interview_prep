list_ = [5,1,4,2,8]
for i in range(0,len(list_)):
    for j in range(0,len(list_)-i-1):
        if list_[j] > list_[j+1]:
            temp = list_[j]
            list_[j] = list_[j+1]
            list_[j+1] = temp
print(list_)