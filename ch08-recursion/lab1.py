#    8.7 LAB: Fibonacci sequence (recursion)
#   
#   The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, for example: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which takes in an index, n, and returns the nth value in the sequence. Any negative index values should return -1.
#   
#   Ex: If the input is:
#   
#   7
#   
#   the output is:
#   
#   fibonacci(7) is 13
#   
#   Note: Use recursion and DO NOT use any loops.

# Solution:

# default cases for bottom and top values per the Fibonacci sequence
def fibonacci(n, bottom = 0, top = 1):

    # negative numbers return -1 as per the instructions
    if n < 0:
        return -1
    
    # base cases
    if n == 0:
        return bottom
    if n == 1:
        return top

    # recursive case, goes until n == 1
    # the algorithm is embedded in the function call
    # and the function call is embedded in a return statement
    return fibonacci(n-1, top, bottom + top)

# End solution

if __name__ == "__main__":
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')