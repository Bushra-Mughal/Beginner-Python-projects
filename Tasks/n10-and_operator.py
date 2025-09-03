#task 1:
num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))
num3=eval(input("Enter third number: "))
if num1>num2:
    if num1>num3:
        print(num1,"is greater.")
elif num2>num1 :
    if num2>num3:
        print(num2,"is greater.")
elif num3>num1:
    if num3>num2:
        print(num3,"is greater.")

#task 2:
marks=eval(input("Enter marks: "))
if marks<=100:
    if marks>=90:
        print("A-1")
    elif marks>=80:
        print("A")
    elif marks>=70:
        print("B")
    else:
        print("Fail")
else:
    print("overflow")

#task 3:
val=int(input("Enter electric units: 120 or 350 or 440 "))
# for units = 120 , 350 , 440 only 
if val<1 and val>=100:
    print(val*2)
elif (val>100 and val<=200):
    a=100*2
    rem=val-100
    b=rem*4
    print(a+b)
elif (val>300 and val<=400):
    a=100*2
    rem=val-100
    b=100*4
    rem=val-100
    c=100*6
    rem=val-100
    d=rem*8
    print(a+b+c+d)
elif (val>300 and val<=400):
    a=100*2
    rem=val-100
    b=100*4
    rem=val-100
    c=100*6
    rem=val-100
    d=100*8
    rem=val-100
    e=rem*10
    print(a+b+c+d+e)


#for units between = 1 - 500 (not only for 120 , 350 , 440 ):

# charges=0
# if (val>=1 and val<=100):  #range = [1,100]
#     print(val*2)
# if(val>100):               #range = (100,200)
#     charges+=100*2
#     val-=100
#     if(val<100):
#         charges+=val*4
#         print(charges)
# if(val>=100):              #range= [200,300)
#     charges+=100*4
#     val-=100
#     if(val<100):
#         charges+=val*6
#         print(charges)
# if (val>=100):            #range = [300,400)
#     charges+=100*6
#     val-=100
#     if(val<100):
#         charges+=val*8
#         print(charges)
# if(val>=100):             #range = [400,500)
#     charges+=100*8
#     val-=100
#     if(val<100):
#         charges+=val*10
#         print(charges)