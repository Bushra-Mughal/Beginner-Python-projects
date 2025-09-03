# GramToKilo
gram=eval(input("Enter grams: "))
print("Kilos are: ", int(gram/1000))
print("Remaining grams are: ",gram%1000)

# InchToFeet
inch=eval(input("Enter inches: "))
print("feets are: ",int(inch/12))
print("Remaining inches are: ",inch%12)

# DaysToMonth
days=int(input("Enter days: "))
print("Months are: ",int(days/30))
print("Remaining days are: ",days/30)

# DaysToWeek
days=int(input("Enter days: "))
print("Weeks are: ",int(days/7))
print("Remaining days are: ",days%7)

# DaysToYear
days=int(input("Enter days: "))
print("Years are: ",int(days/365.5))
print("Remaining days are: ",days%365.5)

# MinutesToHours
min=eval(input("Enter minutes: "))
hrs=min/60 
print("Hours are:  hr",int(min/60))
print("Remaining minutes are: ",min%60)