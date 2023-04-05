import string
n=1
l = string.ascii_lowercase[:1]
o = []
for i in range(5):
    o.append('-'.join(l[::-1][:i+1] + l[n-i:]).center((4*5-3), '-'))

# print(*o,*o[::-1][1:],sep='\n')
# print(" ")
print(*o, *o[::-1][1:], sep = '\n')