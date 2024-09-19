# As repr(), return a string containing a printable representation of an object,
# but escape the non-ASCII characters in the string returned by repr() using \x, \u, or \U escapes.
# This generates a string similar to that returned by repr() in Python 2.

print(ascii("My name is Ståle"))
print(ascii("My name is Виталий"))
print(ascii((1, 2, 3, 'å')))
