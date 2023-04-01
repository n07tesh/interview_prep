
# x = 3.1415926
# y = 12.9999
# print("\nOriginal Number: ", x)
# print("{:.0f}".format(x))
# # print() 
				 

# def reverse_string_words(text):
#     for line in text.split('\n'):
#         return(' '.join(line.split()[::-1]))
# print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
# print(reverse_string_words("Python Exercises."))

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
				 
	