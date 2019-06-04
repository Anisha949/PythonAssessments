#class for catching exceptions
class MyError(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return(repr(self.value))

#function for binary search
def binarySearch(a,l,r,x):
    if r>=l:
        mid =l + (r-1)/2
        mid =int(mid)
#if the middle element itself is the element to be searched return the index
        if a[mid] == x:
            return mid

#if the element to be searched is smaller than the middle element(search the left subpart)
        elif a[mid]>x:
           return binarySearch(a,l,mid-1,x)

#if the element to be searched is larger than the middle element(search the right subpart)
        else:
           return binarySearch(a,mid+1,r,x)

#if element is not found
    else:
        raise MyError(-1)




#input sorted  list(as binary search only works on a sorted list)
a=[2,3,10,40]

#element to be searched
x=20

#sorted array
print(a)

#try-Except for the exception caught
try:
#calling the function for binary search
    index = binarySearch(a,0,len(a)-1,x)
    print('Element found at index: ',index)
except MyError as error:
            print('Element not found')





'''output
Test-case 1 (x=10)
[2, 3, 10, 40]
Element found at index:  2

Test-case 2 (x=20)
[2, 3, 10, 40]
Element not found
'''



