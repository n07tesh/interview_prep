# map() function it is a inbuild python method similiar to zip()
# function and it enables to the zip the elementof the iterable by mapping
# the element of the first iterable with the second iterable element

list_a = [[2,3],[4,5],[6,7]]
list_b = [[4,5],[6,3],[8,9]]
new = list(map(list.__add__,list_a,list_b))
print(new)