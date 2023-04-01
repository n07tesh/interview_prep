# # use the range() and len() function to create a suitable iterate
# from ast import comprehension


# list1 = ['apple','banana','cherry']
# for i in range(len(list1)):
#     print(list1[i])

# #while loop
# list2 = ['apple','banana','cherry']
# i = 0
# while i < len(list2):
#     print(list2[i])
#     i = i + 1

# # List comprehension offers the shortest syntax for looping through list.
# list3 = ['hello','verify','good']
# [print(x) for x in list3]

# list4 = ['apple','banana','mango','cherry','kiwi']
# y = [x for x in list4 if 'a' in x]
# print(y)

# list5 = []
# y = [x for x in range(10) if x <= 5]
# print(y)
# y.sort(reverse=True)
# print(y)

# sort descending
# def myfun(n):
#     return abs(n-50)
# y = [100,50,65,82,23]
# y.sort(key=myfun)
# print(y)


# l1 = ['letter','letter','word','alphabet','word']
# new_dict = {}
# new_l1 = []
# count = 0
# for i in l1:
#     if i in new_l1:
#         count = count + 1
#         new = {i:count}
#         new_dict.update(new)
#     else:
#         new_l1.append(i)
#         count = count +1
#         new = {i:count}
#         new_dict.update(new)
# print(new_dict)




# my_dict = {i:l1.count(i) for i in l1}
# print(my_dict)
# user_input = input("enter the word")
# new1 = []
# for i in l1:
#     if i in user_input:
#         l1.remove(i)
#     # new1.append(i)
# print(list(set(l1)))
from run_time import run_time

@run_time
def binary_search(number_list,number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        if mid_index < number_to_find:
            left_index = left_index + 1
        else:
            right_index = mid_index - 1
    return -1
        

if __name__ == '__main__':
    number_list = [12,45,67,10,98,100,1]
    number_to_find = 100
    obj = binary_search(number_list,number_to_find)
    print(obj)




    

