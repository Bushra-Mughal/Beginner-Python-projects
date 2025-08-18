# to enter emojis ( win + ; )
dic={}
print("😝 Welcome to contact book 😝")
exit=False
while(exit!=True):
    print("\n🟩 1. Add contact\n🟩 2. Search contact\n🟩 3. View all contacts\n🟩 4. Exit")
    opt=int(input("🔴 Enter ( 1 - 4 ): "))
    if opt==1:
        key=input("\tEnter name: ")
        dic[key]=input("\tEnter phone number: ")
        print("📅 Data saved ")
    elif opt==2:
        key=input("\t🔴 Enter name to search: ")
        print("\t🟡 Contact is: ",dic.get(key))
    elif opt==3:
        for key in dic:
            print("\t〰️ Name: ",key,"\t📞 Contact: ",dic[key])
    elif opt==4:
        print("--⭕⭕ Exit ⭕⭕--")
        exit=True
        break
    choice=input("🔴 Want to continue ( Y/N ): ").capitalize()
    if choice=='N':
        print("--⭕⭕ Exit ⭕⭕--") 
        exit=True