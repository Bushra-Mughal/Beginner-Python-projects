class calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        if y!=0:
            return x/y
        else:
            return -1
    def rem(self,x,y):
        return x%y
     
    def run(self):
        ch=int(input("1. ADD\n2. SUB\n3. MUL\n4. DIV\n5. REM\nYour choice:  "))
        a=eval(input("Enter 1st number:  "))
        b=eval(input("Enter 2nd number:  "))
        if ch==1:
            print(self.add(a,b))
        elif ch==2:
            print(self.sub(a,b))
        elif ch==3:
            print(self.mul(a,b))
        elif ch==4:
            print(self.div(a,b))
        elif ch==5:
            print(self.rem(a,b))
        sel=input("Want to continue? ( Y / N ):   ").capitalize()
        if sel=='Y':
            self.run()
        else:
            print("Bye!")

obj=calculator()
obj.run()