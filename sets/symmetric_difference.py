'''
If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) by default. To specify that comma is the delimiter, use string.split(','). For this challenge, and in general on HackerRank, space will be the delimiter.

Usage:

>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']
If the list values are all integer types, use the map() method to convert all the strings to integers.

>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]
Sets are an unordered collection of unique values. A single set contains values of any immutable data type.

CREATING SETS

>> myset = {1, 2} # Directly assigning values to a set
>> myset = set()  # Initializing a set
>> myset = set(['a', 'b']) # Creating a set from a list
>> myset
{'a', 'b'}

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def difference(a,b):
    set_ = set()
    s_m_arr = set(a)
    s_n_arr = set(b)
    set_.update(s_m_arr.difference(s_n_arr))
    set_.update(s_n_arr.difference(s_m_arr))
    for i in sorted(set_):
        print(i)
if __name__ == "__main__":
    M = int(input())
    a = list(map(int,input().split()))
    N = int(input())
    b = list(map(int,input().split()))
    difference(a,b)