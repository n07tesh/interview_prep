# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# list_ = ["flower","flow","flight"]
# temp = []
# length = len(list_)
# for i in range(0,length):
#     print(i)

str = ["flower","flow","floight",'floex']
str.sort()
first = str[0]
last = str[-1]
i=0
while i< len(first) and i < len(last) and first[i] == last[i]:
    i +=1
print(first[:i])



# lngth = len(str)-1
# str.sort()
# temp = []
# i = 0
# for x in range(0,len(str[i])):
#     if str[i][x] == str[i+1][x] and str[i][x] == str[i+2][x]:
#         temp.append(str[i][x])
#     else:
#         if i>lngth:
#             break
#         i+=1
#         continue
# print(''.join(temp))
            
            
