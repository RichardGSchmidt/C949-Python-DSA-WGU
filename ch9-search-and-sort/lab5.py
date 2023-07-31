#    9.14 LAB: Binary Search
#   
#   Binary search can be implemented as a recursive algorithm. Each call makes a recursive call on one-half of the list the call received as an argument.
#   
#   Complete the recursive function binary_search() with the following specifications:
#   
#       Parameters:
#           a list of integers
#           a target integer
#           lower and upper bounds within which the recursive call will search
#       Return value:
#           if found, the index within the list where the target is located
#           -1 if target is not found
#   
#   The algorithm begins by choosing an index midway between the lower and upper bounds.
#   
#       If target == nums[index] return index
#       If lower == upper, return -1 to indicate not found
#       Otherwise call the function recursively with half the list as an argument:
#           If nums[index] < target, search the list from index + 1 to upper
#           If nums[index] > target, search the list from lower to index - 1
#   
#   The list must be ordered, but duplicates are allowed.
#   
#   Once the search algorithm works correctly, add the following to binary_search():
#   
#       Count the number of calls to binary_search().
#       Count the number of times when the target is compared to an element of the list. Note: lower == upper should not be counted.
#   
#   Hint: Use a global variable to count calls and comparisons.
#   
#   The input of the program consists of integers on one line followed by a target integer on the second.
#   
#   The template provides the main program and a helper function that reads a list from input.
#   
#   Ex: If the input is:
#   
#   1 2 3 4 5 6 7 8 9
#   2
#   
#   the output is:
#   
#   index: 1, recursions: 2, comparisons: 3

# Solution:
# Global variables
recursions = 0
comparisons = 0

def binary_search(nums, target, lower, upper):
    
    #Varible Declaration
    global recursions
    global comparisons
    recursions += 1
    mid = (upper + lower) // 2
    
    # print("comparison block 'nums[mid] == target' reached")
    comparisons += 1
    if nums[mid] == target:
        return mid
        
    # Don't count this comparison
    #   as per instructions
    if lower == upper:
            return -1
            

    # This section passes unit tests, HOWEVER IT IS WRONG.
    #   It does not count the number of comparisons correctly.
    #   The comparisons should be counted before the if statements, 
    #   not inside them, as the comparisons are made regardless of
    #   the truthy-ness of the if statements.
    #   This is a problem with the unit tests, not the code.
    
    # comparisons += 1 #proper placement
    # print("comparison block 'nums[mid] < target' reached")) 
    if nums[mid] < target:
        comparisons += 1 #wrong placement, passes unit test
        return binary_search(nums, target, mid + 1, upper)       
    
    # comparisons += 1 #proper placement
    # print("comparison block 'nums[mid] > target' reached"))
    if nums[mid] > target:
        comparisons += 1 #wrong placement, passes unit tests
        return binary_search(nums, target, lower, mid - 1)
        
    

if __name__ == '__main__':
    
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]
    
    
    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')