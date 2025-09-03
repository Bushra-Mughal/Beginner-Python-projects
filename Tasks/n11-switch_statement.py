#task 1:
val=int(input("Enter month: between 1 - 12 "))
match val:
    case v if v==5 or v==6 or v==7:
        print("Summer")
    case v if v==8 or v==9 or v==10:
        print("Automn")
    case v if v==11:
        print("Winter")
    case v if v==2 or v==3 or v==4:
        print("Spring")
    case _:
        print("Invalid")

#task 2:
percentage=int(input("Enter percentage: 39 OR 98 OR 80 "))
match percentage:
    case 39:
        print("Fail")
    case 98:
        print("A-1")
    case 80:
        print("A")
    case _:
        print("No result")