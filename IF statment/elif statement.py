# mark = int(input("enter your percentage::"))
# if mark<34:
#     print("sorry you fail in exam")
# elif mark>=35 and mark<50:
#     print("you got 3rd class")
# elif mark>=50 and mark<60:
#     print("you got 2nd class")
# elif mark>=60 and mark<=100:
#     print("you got 1st class")
# else:
#     print("invalid mark you entered")

# : Find bigger value of two given values
a = int(input("enter 1st value:"))
b = int(input("enter 2st value:"))
if a>b:
    print(a,'is greaterthan',b)
elif b>a:
    print(b,'is greaterthan',a)
else:
    print(a,'&',b ,'both are same')