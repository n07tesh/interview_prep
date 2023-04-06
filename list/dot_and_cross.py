import numpy as np

# Ask the user to input a list of numbers
# num_list = int(input("Enter the number of list"))
# for i in range(num_list):
#     input_str = input("Enter a list of numbers, separated by spaces: ")
#     input_list = input_str.split()

#     # Convert the list of strings to an array of floats
#     input_array = np.array(input_list)

#     # Print the resulting array
#     print("Input array:", input_array)

N = int(input())

A = np.array([input().split() for _ in range(N)],int)
B = np.array([input().split() for _ in range(N)],int)

print(np.dot(A,B))