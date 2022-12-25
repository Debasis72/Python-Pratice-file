# If we need to delete the value 27 from the above dictionary then (by using pop)

a  = {'Id': 100, 'Name': 'Sai', 'subjects': ['SQL Server', 'Oracle', 'Python'], 'Age': 27}
a.pop('Age')
print(a)

# We can also delete by using popitem()
# #this function removes last key:value pair in the dictionary,
a.popitem() 
print(a)

# If we need to delete all key:value pairs then we can use clear()

a.clear() #deleting all pairs, then we can have an empty dict.
print(a) 