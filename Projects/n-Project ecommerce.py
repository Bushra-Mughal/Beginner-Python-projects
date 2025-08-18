print("\n🛒 Welcome to ecommerce website 🕸️")
dic={
    "Jeans": 700,
    "Shirt": 1000,
    "Jacket": 2500,
    "Scarf": 100,
    "Abaya": 1200,
    "Jumper":  2500
}
print("\nMenu available: \n")
for val in dic:
    print("\t\t",val," = Rs:",dic[val])
lis=[]
exit=False
cost=0
while exit!=True:
    item=input("\n\tWhat item do you want:  ").capitalize()
    quantity=int(input("\tHow much do you want:  ( integer )  "))
    lis.append(f" {dic[item]} * {quantity}")
    cost+=(dic[item]*quantity)
    choice=input("\tWant to add more item? ( Y / N )   ").capitalize()
    if choice=='N':
        print("\n\tReceipt: ")
        for val in lis:
            print("\t\t💮",val)
        print(f"\n\tYour order costs: Rs:{cost}")
        print("\tThanks for buying......")
        exit=True