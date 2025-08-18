print("😁 Welcome to restaurant 😁")
dic={
    "Pizza": 600,
    "Pasta": 250,
    "Burger": 450,
    "Salad": 50,
    "Coffee": 220
}
exit=False
order=0
while(exit!=True):
    print("📃 Items we have:")
    for val in dic:
        print("\t\t",val," Rs:",dic[val])
    key=input("\t🟢 Enter name of item to buy: ").capitalize()
    order+=dic.get(key,0)
    print("\t🔵 Your order costs: ","Rs:",order)
    choice=input("❓ Want to add more items? ( Y / N )").capitalize()
    if choice=='N':
        exit=True
print("\n🧾 Payment reciept")
print("\t🟡 Kindly pay: ","Rs:",order,"\n\n\t🙏 Thanks 🙏")