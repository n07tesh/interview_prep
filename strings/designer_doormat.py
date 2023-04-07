'''Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.'''
# n = int(input())
# m = n*3
# print(m)
# mat_size = n * m
# design_ = '.|.'
# for i in range(m+1):
#     m_ = 0
#     if m_ is (m+1 % 2):
#         print("-" + str(design_),end="")
#     print('-',end="")

n,m = list(map(int, input().split()))
a = par = ''
for i in range(n):
    if i == (n//2):
        a = 'WELCOME'
    elif i<(n//2):
        if a == '':
            par = '.|.'
            a = par
        else:
            par += '.|..|.'
            a = par
    else:
        if i == (n//2+1):
            a = par
        else:
            par = par[6::]
            a = par
    print(a.center(m,'-'))

