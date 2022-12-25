a = 10
b = 20
if a>b:
    print("a is graterthan :",b)
elif a<b:
    print("a is lessthan:",b)
else:
    print("both are equal")



# String comparison

# Eg1:
# st1='b'
# st2='a'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')
# Output
# b is bigger than a
# Note: in the above program, we have set st1=’b’ and st2=’a’ when we see the alphabet in ascending
# order( from a to z), then here, ‘b’ is bigger than ‘a’
# Eg2:
# st1='a'
# st2='b'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')
# Output
# b is bigger than a

# Eg3:
# st1='a'
# st2='a'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')
# Output
# both a and a are equal
# Eg4:
# st1='bc'
# st2='ax'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')

# Output:-
# bc is bigger than ax
# Note: interpreter will check only first characters from both strings, so as per first characters, st1 is
# bigger than st2.

# Eg5:
# st1='ax'
# st2='am'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')

# Output:-
# ax is bigger than am
# Note: when the first characters are same in both strings, then interpreter will check the second
# characters. As per second characters interpreter will decide the bigger string in the given two strings.


# Eg6:
# st1='python'
# st2='narayana'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')

# Output:
# python is bigger than narayana
# Note: ‘p’ in the st1 is bigger than ‘n’ in the st2 string. So st1 variable value is bigger than st2 variable

# Eg7:
# st1='1ax'
# st2='am'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')

# Output:-
# am is bigger than 1ax

# Note: here interpreter compares ‘1’ from st1 with ‘a’ from st2 variable.
# Generally characters are bigger than numbers, so st2 variable value is bigger than st1 variable value.

# Eg8:
# st1='2ax'
# st2='2am'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')

# Output:-
# 2ax is bigger than 2am
# Note: in the above example, first two characters are same from both strings, now interpreter decides
# based on third character. ‘x’ is bigger then ‘m’, so st1 variable value bigger than st2 variable value.

# Eg9:
# st1='123'
# st2='a123'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')

# Output:-
# a123 is bigger than 123

# Eg10:
# st1='ax'
# st2='*m'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')

# Output:-
# ax is bigger than *m
# Note: in the above example, characters are bigger than special characters. So here ‘a’ is bigger than ‘a’.


# Eg11:

# st1='1x'
# st2='&am'
# if st1>st2:
#  print(st1,'is bigger than',st2)
# elif st2>st1:
#  print(st2,'is bigger than',st1)
# else:
#  print('both',st1,'and',st2,'are equal')

# Output
# 1x is bigger than &am
# Note: in the above program, interpreter compares ‘1’ from st1 with ‘&’ from st2 .
# Generally integers are bigger than special characters