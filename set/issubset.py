# x.issubset(y) returns True, if x is a subset of y. "<=" is an abbreviation for "Subset of"
a = {1,2,3,4,5}
b = {1,2,3}
print(a.issubset(b))
print(b.issubset(a))
print(a<=b)
print(b<=a)