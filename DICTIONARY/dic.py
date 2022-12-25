# 1. Creating empty dictionary and adding key:value pairs.
a = {}
print(a)
print(type(a))
a['a']=10
a['b']=16
a['c']=13
a['d']=11
print(a)
# 2. Creating a dictionary with dict() function
a = dict([('a',10),('b',20),('c',40)])
print(a)
print(type(a))

# 3. Creating a dictionary with curly braces including key:value pairs
a = {'a':22,'b':11,'c':33,'d':23}
print(a)
print(type(a))

# Accessing data from dictionary
# We can assign values to the keys and later we can fetch values by using Keys 
sd={'Id':100,'Name':'Sai','Age':20,'Marks':90}
print(sd)
print(sd['Id'])
print(sd['Age'])

std={'Id':100,'Name':'Sai', 'subjects':['SQL Server', 'Oracle', 'Python']}
print(std)
print(std['Name'])
print(std['subjects'])
print(std['subjects'][1])

















