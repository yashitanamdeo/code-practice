# Problem Statement: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

# Iterative Way - Complexity: O(n)
def Iterative_reverse(array):
    start = 0
    end = len(array) - 1

    while start < end:
        #traditional swapping
        """ temp = array[start]
        array[start] = array[end]
        array[end] = temp """

        array[start],array[end] = array[end], array[start] #python swapping

        start += 1
        end -= 1
    return array

array = [1,2,3,4]
print(Iterative_reverse(array))



# Python List slicing - Complexity: O(1)
def Slicing_reverse(array):
    return(array[::-1])

array = [1,2,3,4,5,6,7,8,9,10]
print(Slicing_reverse(array))