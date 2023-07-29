#    8.11 LAB: Drawing a right side up triangle
#   
#   Write a recursive function called draw_triangle() that outputs lines of '*' to form a right side up isosceles triangle. Function draw_triangle() has one parameter, an integer representing the base length of the triangle. Assume the base length is always odd and less than 20. Output 9 spaces before the first '*' on the first line for correct formatting.
#   
#   Hint: The number of '*' increases by 2 for every line drawn.
#   
#   Ex: If the input of the program is:
#   
#   3
#   
#   the function draw_triangle() outputs:
#   
#            *
#           ***
#   
#   Ex: If the input of the program is:
#   
#   19
#   
#   the function draw_triangle() outputs:
#   
#            *
#           ***
#          *****
#         *******
#        *********
#       ***********
#      *************
#     ***************
#    *****************
#   *******************
#   
#   Note: No space is output before the first '*' on the last line when the base length is 19.
#   

# Solution:

def draw_triangle(base_len):

    # base case draws the tip of the triangle
    if base_len == 1:
        print (" " * 9 + '*')
        
    # recursive case
    else:
        
        # recursive call (we want the tip drawn first)
        draw_triangle(int(base_len - 2))
        
        # printing script (not casting as int breaks this)
        print (" " * (9 - int(base_len)//2) + '*' * int(base_len))

# End solution

if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)