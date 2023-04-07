_, arr = input(),input().split()
A  = set(input().split())
B = set(input().split())
happiness = 0
for a in arr:
    if a in A:
        happiness +=1
    elif a in B:
        happiness -=1
print(happiness)

