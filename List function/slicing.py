# 1. By using slicing we can fetch set of characters from list.
# 2. It also supports both forward and backward indexing
# 3. Colon (:) is the slicing operator.

a = ['a',10,True,2.5,2+1j]
print(a[:])
print(a[0:])
print(a[-5:])
print(a[-5:-1])

# Using ::
# Syn: [starting_number :: increment_value]
# The default increament value is 1

lst=[10,20,30,40,50,60,70,80,90]
print(lst[::])
print(lst[0::])
print(lst[2::])
print(lst[-9::])
print(lst[-1::])
print(lst[-1::-1])
print(lst[::-1])
print(lst[0::-1])
