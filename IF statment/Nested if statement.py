# checking the eligibility of interview
name = input("please enter your name")
qal = input("please enter your qualification")
yer = int(input("please enter your passing year"))
per = eval(input("please enter your percentage"))

if qal=='btech' or qal=='be':
    if yer>=2018 and yer<=2021:
        if per>=0 and per<35:
            print('hello',name,"you are not eleasible for interview because",per,'too low')
        elif per>=35 and per<50:
            print('hello',name,"you are eligible for interview because",per,'is good')
        elif per>=50 and per<70:
            print('hello',name,"you are eligible for interview because",per,'is very good')
        elif per>=70 and per<=100:
            print('hello',name,"you are eligible for interview because",per,'is too good please come yesterday')
        else:
            print("hello",name,"you enter wrong percentage")

    else:
        print("hello",name,"you are not fresher")
else:
    print("hello",name,"your",qal,"is not eligible")   
print("thank you")