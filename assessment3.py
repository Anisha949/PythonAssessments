
def sortStringArray(lex, alist, n):
#sorting by defining key of lex order
    sort = sorted(alist, key = lambda word: [lex.index(c) for c in word])

    for i in sort:
        print(i)

#new lex order of sorting the input list
lexical = "rcta"

#list to be sorted
input_List = ["car","rat","cat"]

#length of the input list
n = len(input_List)

#passing the parameters to the sort function
sortStringArray(lexical, input_List, n)




