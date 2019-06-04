#Global list (main list)
input_list1=input('Enter the 1st pair')
list1=[input_list1.split()]

#Checking if any common members in the pairs
def connected(item1,item2):
    for i in list1:
        if item1 in i:
            i.append(item2)
            print(list1)
            return

        elif item2 in i:
            i.append(item1)
            print(list1)
            return

        else:
            pair=[item1,item2]
            list1.append(pair)
            print(list1)
            return


#input the total number of pairs
num = int(input("Enter the number of remaining pairs"))

#iterating through the total number of pairs and taking in entries of pairs
for i in range(num):
    entries=input("Enter the pair")
    input_list=entries.split()
#Splitting the two entries in the list
    connected(input_list[0],input_list[1])

print("The total number of employees who are connected to each other: ",len(list1))

#input to check if two members are oonnected
connect_check=input("Enter the members to be checked")
connect_List=connect_check.split()

#iterating for every item in the main list
for i in list1:
#checking for both the members being present in one list to be connected
    if connect_List[0] in i and connect_List[1] in i:
        print("Yes")
        break
#if present in different lists then not connected
    else:
        print("No")
        break


'''Output
Enter the 1st pair Pradnya Anisha

Enter the number of remaining pairs4

Enter the pair Austin Pradnya
[['Pradnya', 'Anisha', 'Austin']]

Enter the pair Melbourne Austin
[['Pradnya', 'Anisha', 'Austin', 'Melbourne']]

Enter the pair Vishal Akash
[['Pradnya', 'Anisha', 'Austin', 'Melbourne'], ['Vishal', 'Akash']]

Enter the pair Rahul Pavan
[['Pradnya', 'Anisha', 'Austin', 'Melbourne'], ['Vishal', 'Akash'], ['Rahul', 'Pavan']]

The total number of employees who are connected to each other:  3
Enter the members to be checked Anisha Melbourne
Yes
'''










