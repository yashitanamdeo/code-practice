# Problem Statement: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

# Iterative Way
def Iterative_reverse(array):
    start = 0
    end = len(array) - 1
    print(end)
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp

        start += 1
        end -= 1
    return array

array = [1,2,3,4]
print(Iterative_reverse(array))