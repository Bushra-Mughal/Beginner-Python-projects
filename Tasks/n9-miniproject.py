print("------Mini project------")
main_opt=int(input("Enter your selection:\n1. calculator\n2. unit-converter\n3. marksheet\n4. atm\n5. troly load\n6. employee salary calculator\n7. positive negative\n8. age comparing\n9. about developer\n10. exit \noption is: "))
if  (main_opt==1):
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
          
if(main_opt==2):
    # FeetToInch
    feet=eval(input("Enter feet: "))
    inch=feet*12
    print(f"Inches are: {inch} inch")

# InchToFeet,
    inch=eval(input("Enter inches: "))
    feet=inch/12
    print(f"Feet are: {feet} ft")

# KiloToGram
    kilo=eval(input("Enter kilos: "))
    gram=kilo*1000
    print(f"Grams are: {gram} gm")

# GramToKilo
    gram=eval(input("Enter grams: "))
    kilo=gram/1000
    print(f"Kilos are: {kilo} kg")

# DaysToMonth
    days=int(input("Enter days: "))
    month=days/30
    print(f"Months are: {month}")

# DaysToWeek
    days=int(input("Enter days: "))
    week=days/7
    print(f"Weeks are: {week}")

# DaysToYear
    days=int(input("Enter days: "))
    year=days/365.5
    print(f"Years are: {year}")

# MinutesToHours
    min=eval(input("Enter minutes: "))
    hrs=min/60 
    print(f"Hours are: {hrs} hr")

# SecondsToMinutes
    sec=eval(input("Enter seconds: "))
    min=sec/60
    print(f"Minutes are: {min} min")

# SecondsToHours
    sec=eval(input("Enter seconds: "))
    hrs=sec/3600
    print(f"Hours are: {hrs} hr")
elif(main_opt==3):
    name=input("Enter name: ")
    fname=input("Enter father's name: ")
    rollno=input("Enter rollno: ")
    dep=input("Enter department: ")
    prog=input("Enter undgraduate program: ")
    gpa=input("Enter current GPA: ")

    print("-----REPORT CARD-----")
    print("Undgraduate program: ",prog)
    print("Department: ",dep)
    print("GPA: ",gpa)
    print("Name: ",name)
    print("Father's name: ",fname)
    print("Rollno: ",rollno)
elif(main_opt==4):
    rupees=int(input("Enter rupees: "))
    print("5000 : ",int(rupees/5000))
    rupees-=(5000*int(rupees/5000))
    print("1000 : ",int(rupees/1000))
    rupees-=(1000*int(rupees/1000))
    print("500 : ",int(rupees/500))
    rupees-=(500*int(rupees/500))
    print("100 : ",int(rupees/100))
    print("remaining rupees are: ",rupees%100)
elif(main_opt==5):
    load=int(input("Enter number of loads: "))
    Total_Income=load*800
    Driver_charges=load*150
    Tax=Total_Income/10
    Diesel_cost=load*210
    Net_income = Total_Income-(Driver_charges+ Tax + Diesel_cost)
    print("Trolley Load Income Report ---")
    print("Total Income = ",Total_Income)
    print("Driver = ",Driver_charges)
    print("Tax 10% = ",Tax)
    print("Diesel = ",Diesel_cost)
    print("Net Income = ",Net_income)
elif(main_opt==6):
    Basic_pay=int(input("Enter Basic Pay: "))
    House_Rent=(45/100)*Basic_pay
    Medical_Allowance=(15/100)*Basic_pay
    Bonus=(5%100)*Basic_pay
    Gross_Pay= Basic_pay+House_Rent+Medical_Allowance+Bonus

    Income_Tax=(5/100)*Basic_pay
    Convance_Allowance=(8/100)*Basic_pay
    Zakat=(2.5/100)*Basic_pay
    Net_income=Gross_Pay-(Income_Tax+Convance_Allowance+Zakat)

    print("------ Salary Slip ------")
    print("Gross Pay: ",Gross_Pay)
    print("-------------------------------")
    print("Net Income: ",Net_income)
elif(main_opt==7):
    num=eval(input("Enter an integer: "))
    if (num>0):
        print("Positive")
    if (num<0):
        print("Negative")
    if (num==0):
        print("Number is zero")
elif(main_opt==8):
    num=int(input("Enter an integer: "))
    if (num==0):
        print("Number is zero")
    if (num%2==0):
        print("Even")
    else:
        print("Odd")
elif(main_opt==9):
    print("My name is Bushra Mughal.Iam a python developer")
elif(main_opt==10):
    print("EXIT")