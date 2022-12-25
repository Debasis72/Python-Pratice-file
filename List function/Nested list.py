'''
lst1 = [1,2,'jack',7,True]
lst2 = [2,3,'jack',00,False]
lst3 = [56,4,'jack',9,99,2+2J]
nested = [lst1,lst2,lst3]
print(nested)
print(nested[0])
print(nested[1])
print(nested[2])
print(nested[2][1])
print(nested[-1][-1])
'''
'''
# Working with index method on nested list: 
List1=[10,'Python',5.5]
List2=[20,30,'Narayana',3+4j]
List3=[1,True,2,'Durga']
NestList=[List1,List2,List3]
print(NestList)
print(NestList.index([20,30,'Narayana',3+4j]))
print(NestList[1].index(30))
print(NestList[-2].index(3+4j))
'''
# Increasing the length of nested list
lst=[5,[2,'a',3],[20,30,40]]
lst[1].append(10)
print(lst)
lst.extend([20])
print(lst)
lst[2].insert(2,True)
print(lst)