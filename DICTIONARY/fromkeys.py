# fromkeys(): we can use tuple elements as keys in the dict and the elements must be unique
a = (1,2,3,4,5)
dic = {}.fromkeys(a,11)
print(dic)

# we can also use list elements as keys in the dict and the elements must be unique
a = [1,2,3,4,5]
b = {}.fromkeys(a,'jack')
print(b)


c=[10,20,30]
d={}.fromkeys(c,'papun')
print(d)