#task 1:
movie1=input("Enter you first movie: ")
movie2=input("Enter you second movie: ")
movie3=input("Enter you third movie: ")
list=[movie1,movie2,movie3]

#task 2:
lis=['a','d','f','c','f','d','a']
copy=lis.copy()
lis.reverse()
if copy==lis:
    print("Yes , it is a palindrome")

#task 3:
tup=('C', 'D', 'A', 'A', 'B', 'B', 'A')
count=0
for val in tup:
    if val=='A':
        count+=1
print("A grades in tuple are: ",count)

#task 4:
tup=('C', 'D', 'A', 'A', 'B', 'B', 'A')
lis=[]
for val in tup:
    lis.append(val)
lis.sort()
print(lis)
