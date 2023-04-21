# n = int(input("enter the element"))
# import random
# random_ = [random(0,20) for _ in range(0,n)]
# print(random_)
####### IDE ISSUE #######
import random as r
  
# Generates a random number between
# a given positive range
r1 = r.randint(5, 15)
print("Random number between 5 and 15 is % s" % (r1))