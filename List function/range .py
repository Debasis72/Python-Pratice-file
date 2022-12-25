'''
We can also use range function to create list
Syn: range(StartingIndexValue, LastValue-1,RangeValue)
Here, both StartingIndexValue and RangeValue are optional.
The default StartingIndexValue is 0.
The default RangeValue is 1
'''
a = tuple(range(10))
print(a)

a = list(range(-10,10))
print(a)

a = list(range(0,10,2))
print(a)