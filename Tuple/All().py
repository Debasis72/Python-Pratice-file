# All(): This function returns True if all elements are true, if any element is false (either 0 or False)
# then it will return Fasle. For empty tuple also it will return True.
a =  (1,2,3,4)
print(all(a))

a =  (1,2,3,4,0)
print(all(a))

a =  ()
print(all(a))