myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
from collections import Counter



print(Counter(myList))

from collections import Counter
sizes = '1 2 3 4 5 6 7 8 9 9'
z = Counter([int(s) for s in sizes.split()])
print(z)