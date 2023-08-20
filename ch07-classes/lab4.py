#   7.14 LAB: Triangle area comparison (classes)
#   Given class Triangle, complete the program to read and set the base and height of triangle1 and triangle2, determine which triangle's area is smaller, and output the smaller triangle's info, making use of Triangle's relevant methods.
#   
#   Ex: If the input is:
#   
#   3.0
#   4.0
#   4.0
#   5.0
#   where 3.0 is triangle1's base, 4.0 is triangle1's height, 4.0 is triangle2's base, and 5.0 is triangle2's height, the output is:
#   
#   Triangle with smaller area:
#   Base: 3.00
#   Height: 4.00
#   Area: 6.00

#Solution is inside the main function.
class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

# Solution
    # Part1: Read and set base and height for triangle1 (use set_base() and set_height())
    triangle1.set_base(float(input()))
    triangle1.set_height(float(input()))
    # Part2: Read and set base and height for triangle2 (use set_base() and set_height())
    triangle2.set_base(float(input()))
    triangle2.set_height(float(input()))
# End solution      
    print('Triangle with smaller area:')  
    
    # TODO: Determine smaller triangle (use get_area())
    #       and output smaller triangle's info (use print_info())
    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info()
    else:
        triangle2.print_info()