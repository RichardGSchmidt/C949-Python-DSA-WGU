#These are my personal notes on the class:

#Quicksort partitions a list into two halfs, one high and one low.
#This list is sorted based on a pivot

#This is my version of the quicksort method ZyBooks teaches:

# It uses two functions, the main quicksort function and
#   a partition function which partitions list values into
#   a low and a high side based on a pivot value.
 
def partition(nums, i, k):
    # We are going to use the midpoint of the range
    #   as this is how the book does it, but any value
    #   between i and k works).
    midpoint = i + (k - i) // 2
    pivot = nums[midpoint]
    low = i
    high = k
    done = False

    while not done:

        while nums[low] < pivot:
            low += 1

        while pivot < nums[high]:
            high -= 1

        if low >= high:
            # If the low index is greater or equal to the high index,
            #   the process is complete so we exit the while loop.
            done = True

        else:
            # Else swap the values (I use tuple assignments here)
            nums[low], nums[high] = nums[high], nums[low]

            # Then increment the low and decrement the high values
            #   to continue 
            low += 1
            high -= 1

    #The return indicates the highest index of the low partition
    return high

# The Quicksort function uses recursion. I've added default values so the
#   initial call of the function can use only the list as an arguement
def QuickSort(nums, i = 0, k = -1):
    # if the default value of k is used we reassign it to the last array index
    if k == -1:
        k = len(nums) - 1

    # Base case if the low is greater than or equal the high
    #   and the list is sorted.
    if i >= k:
        return
    
    # Otherwise, the list is partitioned and the highest index of the low
    #   side is stored in varible j
    j = partition(nums, i, k)

    # Followed by recursively calls on each side of the partion
    QuickSort(nums, i, j)
    QuickSort(nums, j+1, k)

num1 = [54, 21, 11, 11, 58, 27, 34, 548, 41, 21458, 221, 521, 324, 1148]
print(f'Unsorted: {num1}')
QuickSort(num1)
print(f'Sorted: {num1}')