# Index(): this function finds the index value for specific element.
a = ['a',1,2,3,'True',4,56,8,896,'vv']
b = a.index('True')
print(b)

# Index on nested list: 

lst=[10,20,30,40,[50,60,[100,200,300],70],80,90]
b = lst.index(40)
print(b)
c = lst.index(30)
print(c)
d = lst.index(80)
print(d)
e = lst[4][2].index(200)
print(e)
f = lst[4].index(70)
print(f)
g = lst[4].index(90)
print(g)

