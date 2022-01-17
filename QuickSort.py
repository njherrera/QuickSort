# divide and conquer algorithm
# selects pivot element from array and partitions elements according to whether they are greater or less than the pivot element
# sub-arrays are then sorted recursively

# pivot meets following 3 conditions after sorting
    # correct position in final, sorted array
    # items to left are smaller
    # items to right are larger
# move pivot to end of array and look for 2 items:
    # first item, starting from left, that's larger than pivot
    # first item, starting from right, that's smaller than pivot
    # swap items
    # repeat process until item from left has greater index than item from right
    # swap item from left with pivot
# at this point, all items to left of pivot are smaller and all items to right of pivot are larger

# PSUEDOCODE

# params: array = unsorted array, low = lowest index, high = highest index
# QUICKSORT (array, low, high)
    # if (low < high)
        #  pivot_index = partition (array, low, high)
        # quickSort (array, low, pivot_index - 1)
        # quickSort (array, pivot_index + 1, high)

# same params as quicksort
# selects pivot as middle element
# PARTITION (array, low, high)
    # pivot = array[floor((high + low) / 2)
    # i = low - 1
    # j = high + 1

    # while array[i] < pivot
        # i++

    # while array[j] > pivot
        # j--

    # if i >= j
        # return j

    # swamp array[i] with array[j]


