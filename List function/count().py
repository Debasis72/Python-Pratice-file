# Count(): this function counts the no.of occurrences of specific element in the list.






# a = ['a','a','b',1,2,3,4,4,4,4]
# b = a.count(4)
# print(b)

# a = ['a','a','b',1,2,3,4,4,4,4]
# b = a.count('a')
# print(b)

from typing import Counter
a = 'abababacbcbcbccacacacaefde'
b = Counter(a)
print(b)
c = b.most_common(2)
print(c)
d = sorted(b)
print(d)
e = ''.join(sorted(b.elements()))
print(e)
f = sum(b.values())
print(f)
