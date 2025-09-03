#task 1:
rupees=int(input("Enter rupees: "))
print("5000 : ",int(rupees/5000))
rupees-=(5000*int(rupees/5000))
print("1000 : ",int(rupees/1000))
rupees-=(1000*int(rupees/1000))
print("500 : ",int(rupees/500))
rupees-=(500*int(rupees/500))
print("100 : ",int(rupees/100))
print("remaining rupees are: ",rupees%100)


#task 2:
Java=int(input("Enter Java Marks: "))
Oracle=int(input("Enter Oracle Marks:")) 
Cp=int(input("Enter C Marks: "))
Database=int(input("Enter Database Marks: "))
Cpp=int(input("Enter C++ Marks: "))
obtain=Java+Oracle+Cp+Database+Cpp
print("---------------------------")
print("Obtain Marks = ",obtain)
print("Total Marks = 500")
print("Percentage = ",(obtain/500)*100,"%")


# #task 3:
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


#task 4:
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