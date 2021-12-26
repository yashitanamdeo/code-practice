# Problem Statement: https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

# Linear Search Method - Complexity: O(n)
def LinearSearch(array):
    minimum = array[0]
    maximum = array[0]
    for element in array:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element
        else:
            pass
    return minimum, maximum

array = [5,4,9,6,7,1,3]
Min, Max = LinearSearch(array)
print("Min: ", Min)
print("Max: ", Max)