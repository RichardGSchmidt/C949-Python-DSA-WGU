#    9.10 LAB: Descending selection sort with output during execution
#   
#   Write a program that takes an integer list as input and sorts the list into descending order using selection sort. The program should use nested loops and output the list after each iteration of the outer loop, thus outputting the list N-1 times (where N is the size of the list).
#   
#   Ex: If the input is:
#   
#   20 10 30 40
#   
#   the output is:
#   
#   [40, 10, 30, 20]
#   [40, 30, 10, 20]
#   [40, 30, 20, 10]
#   
#   Ex: If the input is:
#   
#   7 8 3
#   
#   the output is:
#   
#   [8, 7, 3]
#   [8, 7, 3]
#   
#   Note: Use print(numbers) to output the list numbers and achieve the format shown in the example.

# Solution:

# Helper Function
def Desc_Sel_Sort(arr=[]):

    # this function does not modify the original array
    nums = arr[:]
    for i in range(len(nums) - 1):
        largest = i
        for j in range(i+1, len(nums)):
            if nums[j] > nums[largest]:
                largest = j

        # swap variables on one line using tuple unpacking
        nums[largest], nums[i] = nums[i], nums[largest]

        # print the list once per outer loop iteration
        print(nums)

# Main Block
in_vals = []
for in_val in input().split():
    in_vals.append(int(in_val))
Desc_Sel_Sort(in_vals)


# End solution