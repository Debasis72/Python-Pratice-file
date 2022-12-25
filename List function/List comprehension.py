'''
it provides an easy way to create list objects from any iterable objects based on some conditions.
Syntax: list=[expression for iterative_item in list if condition]
'''
# How to display squares for all even elements in the given list?
lst = [1,2,3,4,5]
lst1 = [x*x for x in lst]
print(lst1)

lst1 = [x*x for x in lst if x%2==0]
print(lst1)
# How to display all unmatching elements from list1, those elements must not be in list2?
lst1=[1,2,3,4,5]
lst2=[1,2,3,6,9]
lst = [i for i in lst1 if i not in lst2]
print(lst)

