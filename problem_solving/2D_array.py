## creating a 2d array


# rows, cols = (5, 5)
# for i in range(5):
#     arr = [[i]*cols]*rows
#     print(arr)


## find the size of matrix
## Approach 1
import numpy as np
a = np.array([[[1,2,3],[1,2,3]],[[12,3,4],[2,1,3]]])
print("shape = ",np.shape(a))
print("dimensions = ",len(a.shape))


## Approach 2
#updating the array
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr, "before")
 
arr[0][0] = 1 # update only one element
print(arr, "after")

x = (5-2)*(5-2)
print(x)

# sum of 2d array
def sum():
    pass

if __name__ == "__main__":
    sum()

def hourglassSum(arr):
    # Write your code here
    max_sum = 0
    row , col = len(arr), len(arr[0])
    for i in range(0,row-2):
        for j in range(0,col-2):
            sum_ = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                  arr[i+1][j+1] + \
                  arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum_>max_sum:
                max_sum=sum_
            else:
                continue
    return max_sum
            # If previous sum is less
            # then current sum then
            # update new sum in max_sum
          
    

if __name__ == '__main__':
    arr =[[1, 2, 3, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 1, 4, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0]]
    # R = 5
    # C = 5
    x = hourglassSum(arr)
    print(f"Maximum sum of hour glass = {x}")