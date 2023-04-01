# def number(num_range):
#     num_list = []
#     for i in range(0,num_range):
#         number_list =int(input("enter the number"))
#         num_list.append(number_list)
#     print("max : ",max(num_list))
#     print("min : ",min(num_list))

# if __name__ == '__main__':
#     num_range = int(input("enter the number"))
#     number(num_range)
a = []
n = int(input("Enter the number"))
for i in range(0,n):
    b = int(input("enter the value"))
    a.append(b)
a.sort()
print(a)