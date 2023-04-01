def bubble_sort(alist):
    for i in range(0,len(alist)):
        for j in range(0,len(alist)-i-1):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    return alist
if __name__ == '__main__':
    alist = [5,1,4,2,8]
    soted = bubble_sort(alist)
    print(soted)