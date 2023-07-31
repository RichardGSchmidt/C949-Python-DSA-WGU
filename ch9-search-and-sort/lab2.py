#    9.12 LAB: Insertion sort
#   
#   The script has four steps:
#   
#       Read a list of integers (no duplicates).
#       Output the numbers in the list.
#       Perform an insertion sort on the list.
#       Output the number of comparisons and swaps performed during the insertion sort.
#   
#   Steps 1 and 2 are provided in the script.
#   
#   Implement step 3 based on the insertion sort algorithm in the book. Modify insertion_sort() to:
#   
#       Count the number of comparisons performed.
#       Count the number of swaps performed.
#       Output the list during each iteration of the outside loop.
#   
#   Implement step 4 at the end of the script.
#   
#   Hints: In order to count comparisons and swaps, modify the while loop in insertion_sort(). Use global variables for comparisons and swaps.
#   
#   The script includes three helper functions:
#   
#       read_nums() # Read and return a list of integers.
#       print_nums(nums) # Output the numbers in nums
#       swap(nums, n, m) # Exchange nums[n] and nums[m]
#   
#   Ex: When the input is:
#   
#   3 2 1 5 9 8
#   
#   the output is:
#   
#   3 2 1 5 9 8
#   
#   2 3 1 5 9 8
#   1 2 3 5 9 8
#   1 2 3 5 9 8
#   1 2 3 5 9 8
#   1 2 3 5 8 9
#   
#   comparisons: 7
#   swaps: 4



def read_nums():
    """Read numbers from input and return them in a list"""
    return [int(num) for num in input().split()]

def print_nums(nums):
    """Output numbers, separating each item by a spaces;
    no space or newline before the first number or after the last."""
    print(' '.join([str(n) for n in nums]), end='')

def swap(nums, n, m):
    """Exchange nums[n] and nums[m]"""
    nums[n], nums[m] = nums[m], nums[n]


def insertion_sort(numbers):
    """Sort the list numbers using insertion sort"""

# Solution:

    # Declare global variables
    global comparisons
    global swaps
    swaps = 0
    comparisons = 0

    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part
        #   stopping once numbers[i] is in correct position

        # Counts the first comparison of the while loop
        comparisons += 1

        while j > 0 and numbers[j] < numbers[j - 1]:

            # Counts every time the while loop is entered
            #   except for the first time per itteration. 
            #   Which is every comparison except for the 
            #   first one (which always evaluates, even 
            #   if this loop is never entered).
            comparisons += 1 if j > 1 else 0

            # Counts every time a swap is performed
            swaps += 1            
            swap(numbers, j, j - 1)
            j -= 1

        # Output the list after each iteration of the outer loop
        #   and a empty print to put a newline between each iteration
        print_nums(numbers)
        print()

# pause solution - continued below

if __name__ == '__main__':
    # Step 1: Read numbers into a list
    numbers = read_nums()

    # Step 2: Output the numbers list
    print_nums(numbers);
    print(end='\n\n')

    # Step 3: Sort the numbers list
    insertion_sort(numbers)
    print()

# Solution continued:    
    # Step 4: Output the number of comparisons and swaps performed
    # Prints global varibles comparisons and swaps
    print(f'comparisons: {comparisons}')
    print(f'swaps: {swaps}')
# End solution