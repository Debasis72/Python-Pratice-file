# Discard(): it will remove elements from the set, if that element is not fund in the set then it will do nothing.
a = {1,2,3,4,5,6,True}
a.discard(True)
print(a)

'''
the difference between remove() and discard() is,

remove(): if we take the element which is not there in the set then it will throw error.

discard(): if we take the element which is not there in the set then it will do nothing, means it will not
throw error
'''