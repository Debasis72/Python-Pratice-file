# a = int(input("enter your mark:-"))
# if a>=35:
#     print("you are pass")

# compare values and display message

# a = int(input("enter 1st number"))
# b = int(input("enter 2nd number"))
# c = int(input("enter 3rd number"))
# if a>b>c:
#     print(a,'is greaterthan',b ,'and',c)

# # : if name is more then or one character then do all string methods
a = input("enter your fast name")
if len(a)>0:
    print(a)
    print(a.capitalize())
    print(a.lower())
    print(a.islower())
    print(a.upper())
    print(a.isupper())
    print(len(a))
    print(a.title())
    print(''.join(sorted(a)))
    print(''.join(reversed(a)))
    print(''.join(reversed(sorted(a))))



