import textwrap
value =  """This function wraps the input paragraph such that each line
in the paragraph is at most width characters long. The wrap method
returns a list of output lines. The returned list
is empty if the wrapped
output has no content."""



wrapper = textwrap.TextWrapper(width=50)
wrapper_dedent = textwrap.dedent(text = value)
original = wrapper.fill(text=wrapper_dedent)

print('Original:\n')
print(original)
  
shortened = textwrap.shorten(text=original, width=100)
shortened_wrapped = wrapper.fill(text=shortened)
  
print('\nShortened:\n')
print(shortened_wrapped)

