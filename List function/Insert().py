# Insert(): this function adds a element at any required index place in the existing list.
# Syn: insert(index_number,element(s))
# Increasing the length of the list

lst=[10,20,'Python',30,True,'Narayana',10,3+4j]
lst.insert(2,5)
print(lst)

lst=[10,20,'Python',30,True,'Narayana',10,3+4j]
lst.insert(2,'jack')
print(lst)

lst=[10,20,'Python',30,True,'Narayana',10,3+4j]
lst.insert(0,[2,'jack',44])
print(lst)