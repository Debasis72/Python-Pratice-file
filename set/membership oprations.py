s={10,20,30,True,100,'Narayana','Python'}
a = 10 in s
print(a)
a = True in s
print(a)
a = 'Python' in s
print(a)
a = 'Narayana' not in s
print(a)

# Removing duplicate elements from other sequence
a = [1,1,2,3,45,66,66,77,88,88]
b = list(set(a))
print(b)

a = (1,1,1,2,2,2,3,3,3,3)
b = list(set(a))
print(b)

a = 'narayana'
b = list(set(a))
c = ''.join(b)
print(c)