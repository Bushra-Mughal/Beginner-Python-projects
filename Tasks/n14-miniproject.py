#Due to default constructor , value is comming without object.

class miniproject:
    def add(self):
        print(10+5)
    def sub(self):
        print(10-5)
    def mul(self):
        print(10*5)
    def div(self):
        print(10/5)
    def trolley_load(self):
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
    def atm(self):
        rupees=int(input("Enter rupees: "))
        print("5000 : ",int(rupees/5000))
        rupees-=(5000*int(rupees/5000))
        print("1000 : ",int(rupees/1000))
        rupees-=(1000*int(rupees/1000))
        print("500 : ",int(rupees/500))
        rupees-=(500*int(rupees/500))
        print("100 : ",int(rupees/100))
        print("remaining rupees are: ",rupees%100)
    def marksheet(self):
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
    def emp_salary(self):
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
    def number_compare(self):
        num=eval(input("Enter an integer: "))
        if (num>0):
            print("Positive")
        if (num<0):
            print("Negative")
        if (num==0):
            print("Number is zero")

obj=miniproject()
print("\nCalculator-------")
obj.add()
obj.sub()
obj.mul()
obj.div()
print("\nMarksheet-------")
obj.marksheet()
print("\nSalary-------")
obj.emp_salary()
print("\nTrolley load-------")
obj.trolley_load()
print("\nNumber compare-------")
obj.number_compare()
print("\nATM-------")
obj.atm()