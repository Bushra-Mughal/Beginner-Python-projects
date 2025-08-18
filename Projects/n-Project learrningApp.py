print(" 😁----- Welcome to python learning app -----😁")

dic={"dictionary": """Definition: \n\tA dictionary in Python is a mutable, unordered collection of key-value pairs where key must be 'unique' and 'immutable' (ie: string, number) and value can be of any data type.\nFeatures: \n\tCreate dictionary with { } or dict().\n\tAccess data through keys. For example: my_dict["name"] → "Alice"\n\tIs mutable. We can add/update items with: my_dict["new_key"] = value\nSyntax:  \n\tdic={ } -> an empty dictionary\n\tdic={ " key ": value,"key 2": value}""",
     "set": """Definition: \n\tA set is an unordered collection of unique elements (like a math set).Set stores unique values , rather than key-value pairs in dictionary.\nFeatures: \n\tAutomatically removes duplicates.\n\tIs unordered. No index-based access (unlike lists).\n\tIs mutable: Can add/remove items.\nSyntax: \n\tset={ 0 }  -> empty set\n\tset={1,23,1,0}  -> this will store= 1, 23 , 0"""
     }
user_dic={}

exit=False
while(exit!=True):
    try:
        opt=int(input("\n\nWhat do you want:\n\t1. Learn dictionary and sets\n\t2. Start a quiz\n\t3. Create dictionary\n\t4. Find in dictionary\n\t5. Show dictionary\n\t6. Quit\n\tOption:  "))
        
        if(opt==1):
            choice=input("\n\ta. Learn dictionary\n\tb. Learn set\n\tOption:  ").capitalize()
            if (choice=='A'):
                print("\n",dic["dictionary"])
            elif (choice=='B'):
                print("\n",dic["set"])
        
        elif(opt==2):
            score=0
            print("\nNote: You have to answer 5 mcqs on python dictionary.")
            ans=input("\nQ1: What is a Python dictionary?\nA) An ordered collection of key-value pairs\nB) An unordered collection of unique keys mapped to values\nC) A list with index-value pairs\nAnswer:  ").capitalize()
            if(ans=='B'):
                print("Correct!")
                score+=1
            else:
                print("Incorrect")
            ans=input("\nQ2: How do you access a value in a dictionary?\nA) dict.get(key)\nB) dict[key]\nC) Both A and B\nAnswer:   ").capitalize()
            if(ans=='C'):
                print("Correct!")
                score+=1
            else:
                print("In complete")
            ans=input("\nQ3: What happens if you try to access a non-existent key with dict[key]?\nA) Returns None\nB) Raises KeyError\nC) Automatically adds the key with a None value\nAnswer:     ").capitalize()
            if(ans=='B'):
                print("Correct!")
                score+=1
            else:
                print("Incorrect")
            ans=input("\nQ4: Which method removes a key and returns its value?\nA) dict.pop(key)\nB) dict.remove(key)\nC) dict.delete(key)\nAnswer:    ").capitalize()
            if(ans=='A'):
                print("Correct!")
                score+=1
            else:
                print("Incorrect")
            ans=input("\nQ5: What is the output of len( {'a': 1, 'b': 2 } )?\nA) 1\nB) 2\nC) 4\nAnswer:    ").capitalize()
            if(ans=='B'):
                print("Correct!")
                score+=1
            else:
                print("Incorrect")
            print("\n\tYour score is: ",score)
            if(score<=2):
                print("\tKeep practicing! ")
            else:
                print("\tKeep it up!")
        
        elif(opt==3):
            print("\nLet's create your own dictionary!")
            print("Start by entering a key along with it's value: ")
            key=input("\tKey 1: ")
            value=input("\tValue: ")
            user_dic[key]=value
            choice=input("\nWant to add more? ( y / n )\nAnswer:  ").capitalize()
            if(choice=='Y'):
                choice=int(input("\nHow many pairs do you want to add? ( integer only )\nAnwer:  "))
                for loop in range(1,choice+1):
                    key=input(f"\nEnter key {loop}: ")
                    value=input("\tEnter value: ").capitalize()
                    user_dic[key]=value
            print("\nEntry successfully saved!")

        elif(opt==4):
            if(len(user_dic)!=0):
                key=input("\nEnter key to find value in dictionary:  ")
                if key in user_dic.keys():
                    print(f"The value is:  {user_dic[key]}")
                else:
                    print("Key not found")
            else:
                print("First create a dictionary.")
        
        elif(opt==5):
            if(len(user_dic)!=0):
                print("\nYour dictionary: ")
                for key in user_dic:
                    print(f"\n\t{key}: {user_dic[key]}")
            else:
                print("Your dictionary is empty")
            
        elif(opt==6):
            exit=True
            print("\nExit app")
        else:
            print("\n\tINVALID")

    except Exception as e:
        print(f"\n\tError: {e}")