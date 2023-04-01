def palindrome(strs):
    if (strs==strs[::-1]):
        print("the given string is palindrome")
    else:
        print("the given string is not palindrome")

if __name__ == '__main__':
    strs = 'namana'
    palindrome(strs)