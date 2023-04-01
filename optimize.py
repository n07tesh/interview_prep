tuple_ = [(2,1,4,3),(2,1,4,3),(1,0,5,2)]
l = []
for x in tuple_:
    s = sorted(x)
    q = tuple(s)
    l.append(q)
    # for i in x:
    #     pass
print(l)
     