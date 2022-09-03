#Finding the kth largest & kth smallest ele in an array
def findkLargeset(k, array):
    # sort the array in descending order
    array.sort(reverse=True)

    # Since indexing start from 0, hence if user want first number, that means index=0
    print("K th largeset element is: ", array[k - 1])


def findkSmallest(k, array):
    # sort the array in ascending order
    array.sort()

    # Since indexing start from 0, hence if user want first number, that means index=0
    print("K th smallest element is: ", array[k - 1])


array = [1, 7, 6, 8, 9, 2, 4, 5, 3, 0]
k = 1

# call function findkmax
findkLargeset(k, array)

# call function findkmin
findkSmallest(k, array)