def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        temp = []
        temp.append(arr[0])
        arr.pop(0)
        arr.append(temp[0])
    return arr

if __name__=="__main__":
    d = 4 #rotations
    arr = [1,2,3,4,5]
    rotateLeft(d,arr)


for value in (arr[d:] + arr[0:d]): 
    print(value)

# Good Approach
arr = [1,2,3,4,5]
d=4
for value in (arr[d:] + arr[0:d]): 
    print(value)