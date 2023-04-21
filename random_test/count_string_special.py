string  = "Py!th#onD%evelo&per_s "
# import ascii 
# count number of symbols
count = 0
for i in string:
    # if ord(i)>65:
    if i.isalpha():
        continue
    else:
        count +=1
print(count) 