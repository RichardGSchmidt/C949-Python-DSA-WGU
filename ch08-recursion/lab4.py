#    8.10 LAB: Count the digits
#   
#   Write a recursive function called digit_count() that takes a positive integer as a parameter and returns the number of digits in the integer. Hint: The number of digits increases by 1 whenever the input number is divided by 10.
#   
#   Ex: If the input is:
#   
#   345
#   
#   the function digit_count() returns and the program outputs:
#   
#   3

# Solution:
def digit_count(num, count=0):
    
    # base case
    if (count == 0 and num == 0):
        return 1
    if num == 0:
        return count
    
    # recursive case
    else:
        return digit_count(num//10, count+1)
# End solution

if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)