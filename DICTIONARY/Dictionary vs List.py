a = [1,2,3,4,5,6]
b = [1,3,2,4,6,5]
print(a==b)
# Note: lst1 and lst2 are containing same elements but in different places, so both lst1 and lst2 are not equal

dict1={"Id":100,"Name":"Sai","Loc":"Hyd","Company":"TCS"}
dict2={"Name":"Sai","Id":100,"Company":"TCS","Loc":"Hyd"}
print(dict1)
print(dict2)
print(dict1==dict2)
# Note: dict1 and dict2 are containing same key-value pairs and also all are in different places, so both dict1 and dict2 are same. In dictionary the order is not fixed.
