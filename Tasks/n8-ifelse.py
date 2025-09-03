#task 1:
num=eval(input("Enter an integer: "))
if (num>0):
    print("Positive")
if (num<0):
    print("Negative")
if (num==0):
    print("Number is zero")

#task 2: 
age1=int(input("Enter first age: "))
age2=int(input("Enter second age: "))
if (age1>age2):
    print("Greater is age 1")
elif (age2>age1):
    print("Greater is age 2")
else:
    print("Both are equal")

#task 3:
num=int(input("Enter an integer: "))
if (num==0):
    print("Number is zero")
if (num%2==0):
    print("Even")
else:
    print("Odd")
#task 4:
opt=int(input("Enter your option:\n1. Add\n2. Substract\n3. Multiplication\n4. Division\n5. Remainder\noption is: "))
num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))
if(opt==1):
    print(num1+num2)
elif (opt==2):
    print(num1-num2)
elif (opt==3):
    print(num1*num2)
elif (opt==4):
    print(num1/num2)
elif (opt==5):
    print(num1%num2)
else:
    print("Invalid selection")


