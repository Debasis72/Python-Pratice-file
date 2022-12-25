# Isdisjoint(): this function returns True if both are empty sets or if both sets contains non-matching elements.
a = set()
b = set()
c = a.isdisjoint(b)
print(c)

a = {1,2,3}
b = {1,2,3}
c = a.isdisjoint(b)
print(c)

a = {1,2,3}
b = {1,2,3,4}
c = a.isdisjoint(b)
print(c)