"""Task 1:  Take user input. Output should be:
                
            user = 3

            ODD EVEN
            1   2   
            3   4
"""
###SOLUTION:

user=int(input("Enter any no: "))
print("Odd\tEven")
for val in range(1,user+1,2):
    print(val,"\t",val+1)



"""Task 2:  Take user input and print square ie:

            user = 3

            1   1
            2   4
            3   9
"""
##SOLUTION:

user=int(input("Enter a number: "))
for val in range(1,user+1):
    print(val,"  ",val*val)



"""Task 3:  Take user input and print:

            user = 3

            1   1   1
            2   4   8
            3   9   27
"""
##SOLUTION:

user=int(input("Enter a number: "))
print("Number\tSquare\tCube")
for val in range(1,user+1):
    print(val,"\t",val*val,"\t",val*val*val)



"""Task 4:  Output should be:
            
            user = 3

            bushra mughal
            bushra mughal mughal
            bushra mughal mughal mughal

"""
##SOLUTION:

user=int(input("Enter value: "))
name="bushra"
surname="mughal"
for i in range(0,user): 
    print(name,end = " ")
    for j in range(0, i+1): 
        print(surname,end = " ")
    print()



"""task 5:  Print letters present in user name
"""
##SOLUTION:

name=input("Enter any name: ")
for val in name:
    print(val)



"""task 6:  Print table till a number 'counter'
"""
##SOLUTION:

table=int(input("Enter number for table: "))
counter=int(input("Enter number for counter: "))
for val in range(1,counter+1):
    print(table," x ",val," = ",table*val)
    


"""task7:   Take a user input and draw a paramid.ie:

            user = 3

            *
            **
            ***
"""
##SOLUTION:

num=int(input("Enter number to print pattern: "))
for i in range(0,num):
    for j in range(0, i+1):
        print("*",end=" ")
    print()



"""task 8:  take user input and print factorial.Output should be:

            user = 3
            1 = 1
            1 * 2 = 2
            1 * 2 * 3 = 6
"""
##SOLUTION:

user=int(input("Enter number to print factorial: "))
for i in range(1, user+1):
    mul = 1
    for j in range(1, i+1):
        mul *= j
        print(j, end = " ")
        if j != i:
            print("*", end = " ")
    print("=" , mul)

