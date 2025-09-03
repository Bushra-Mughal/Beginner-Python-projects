#task 1:
table=int(input("Table till: "))
counter=int(input("Each table till: "))
for v in range(2,table+1):
    for v1 in range(1,counter+1):
        print(v," x ",v1," = ",v*v1)
        
#task 2:
first_row=int(input("Enter number of stars in first row of pyramid: "))
for v in range(first_row,0,-1):
    for v2 in range(1,v+1):
        print(" * ",end=" ")
    print()

#task 3:
num=int(input("Enter any number: "))
for v in range(num,0,-1):
    for v2 in range(1,v+1):
        print(v2,end=" ")
    print()

#task 4: 
rows=int(input("Enter number of rows: "))
col=int(input("Enter number of coloums: "))
for v in range(1,rows+1):
    for v2 in range(1,col+1):
        print("*",end=" ")
    print()

#task 5:
num=int(input("Enter any number: "))
print(2)
for v in range(3,num+1):
    comp=False
    for P in range(2,v):
        if v%P==0:
            comp=True 
    if comp==False:
        print(v)

#task 6:
name=input("Enter name: ")
for v in range(len(name),0,-1):
    print(name[0:v])

#task 7:
letter =input("Enter last alphabet: ").upper()
for v in range(ord(letter),64,-1):
    for v2 in range(65,v+1):
        print(chr(v2),end=" ")
    print()
