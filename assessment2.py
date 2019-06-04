#Function for merging two lists taken as an input
def mergelist(list1,list2):
    merge_list = [(list1[i], list2[i]) for i in range(0,len(list1))]
    return merge_list


#The main function
def main():
#User inputs for list1
    inputList1 = input("Enter the elements of the first list")
#converting the string of input into a list
    list1=inputList1.split()
#User inputs for list1
    inputList2 = input("Enter the elements of the second list")
#converting the string of input into a list
    list2=inputList2.split()

#Calling for the function to merge the two input lists
    final_list= mergelist(list1,list2)
    print("Initial list of tuples to be sorted")
    print(final_list)

#Sorting based on the last element of the list of tuple(-1)
    output = sorted(final_list, key=lambda x:x[-1])
    print("Sorted List of tuples based on the last element")
    print(output)



if __name__ == '__main__':
    main()

'''output
Test case 1
Initial list of tuples to be sorted
[('1', 'ghf'), ('2', 'egf'), ('3', 'hij'), ('4', 'abc')]
Sorted List of tuples based on the last element
[('4', 'abc'), ('2', 'egf'), ('1', 'ghf'), ('3', 'hij')]

Test case 2
Initial list of tuples to be sorted
[('1', '9'), ('2', '8'), ('3', '7'), ('4', '6')]
Sorted List of tuples based on the last element
[('4', '6'), ('3', '7'), ('2', '8'), ('1', '9')]
'''
