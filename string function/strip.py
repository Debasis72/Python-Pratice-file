# . lstrip(): this function removes specific special character to left side of given string.
a = "$$$$python@@@@@"
b = a.lstrip('$')
print(b)
# . rstrip(): this function removes specific special character to the right side of given string
a = "$$$$python@@@@@"
b = a.rstrip('@')
print(b)
# .strip(): this function removes specific special character from both sides to the given string.
a = "$$$$python$$$$@@@"
b = a.strip('$,@')
print(b)


