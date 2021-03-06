# Recursive Python program for insertion sort
# Recursive function to sort an array using insertion sort


def insertion_Sort_Recursive(arr, n):
    # base case
    if n <= 1: return

    # Sort first n-1 elements
    insertion_Sort_Recursive(arr, n - 1)
    '''Insert last element at its correct position
        in sorted array.'''
    last = arr[n - 1]
    j = n - 2

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while (j >= 0 and arr[j] > last):  #GREATER OR LESSER
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last

    # A utility function to print an array of size n
    return (arr)


# Driver program to test insertion sort
arr = [12, 11, 13, 5, 6]
n = len(arr)
print(insertion_Sort_Recursive(arr, n))

# Contributed by Harsh Valecha