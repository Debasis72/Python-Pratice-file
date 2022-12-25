# x.issuperset(y) returns True, if x is a superset of y. ">=" is an abbreviation for "issuperset of"
a = {1,2,4,3,5}
b = {2,1,3}
print(a.issuperset(b))
print(b.issuperset(a))
print(a>=b)
print(b>=a)