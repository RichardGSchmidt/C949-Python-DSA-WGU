#   10.7 LAB: Introduction to data structures labs
#  Step 1: Producing correct output
#  
#  Three commented-out lines of code exist in the main part of the program. Uncomment the lines and click the "Run program" button. Verify that the program's output is:
#  
#  2 + 2 = 4
#  Unknown method: print_plus_2
#  Secret string: "abc"
#  
#  Submit your code for grading. Your submission will pass the "Compare output" test only, achieving 1 of the possible 10 points.
#  Step 2: Inspecting the LabPrinter class
#  
#  Inspect the LabPrinter class implemented in the LabPrinter.py file. Access LabPrinter.py by clicking on the orange arrow next to IntroToDSELabs.py at the top of the coding window. Instance methods print_2_plus_2() and print_secret() print strings using print().
#  Step 3: Implementing call_method_named()
#  
#  Remove the three uncommented lines from the main part of the program. Then implement the call_method_named() function in IntroToDSELabs.py to handle three cases:
#  
#      If method_name is "print_2_plus_2", call printer's print_2_plus_2() instance method.
#      If method_name is "print_secret", call printer's print_secret() instance method.
#      If method_name is anything other than the two strings mentioned above, print "Unknown method: xyz", where xyz is method_name's value.
#  
#  After implementing call_method_named(), click the "Run program" button. Verify that the program's output is, once again:
#  
#  2 + 2 = 4
#  Unknown method: print_plus_2
#  Secret string: "abc"
#  
#  Step 4: Submitting code for 10/10 points
#  
#  Once call_method_named() is properly implemented, submitting the code should receive 10 out of 10 points. The program's output is exactly the same as the implementation from step 1. But step 3's implementation uses the LabPrinter object and step 1 does not.
#  Step 5: Understanding the difference
#  
#  The unit test uses a different implementation of LabPrinter than what's shown in LabPrinter.py. Calls to each instance method are tracked, so the unit test determines whether or not call_method_named() was actually implemented according to lab requirements.
#  
#  Most labs in this material are similar. Program output matters, but how the output is achieved matters more. Functions you implement will commonly require use of an object passed as a parameter.

# Solution:  

# The point of this lab is to make sure you understand that proper implemntation of functions matters as much as output.
# It doesn't have a whole lot to do with the program material, it's just to make sure you understand the grading critera before going deeper into the course.

# This will only run in the ZyLabs environment.
from LabPrinter import LabPrinter

def call_method_named(printer, method_name):
    if method_name == 'print_2_plus_2':
        printer.print_2_plus_2()
    elif method_name == 'print_secret':
        printer.print_secret()
    else:
        print(f'Unknown method: {method_name}')
        
    # Only implement this function after completing step 1
    return

if __name__ == '__main__':
    printer = LabPrinter("abc")
    
    # Step 1:
    # Uncomment the three lines below and submit code for grading. Note that
    # the submission passes the "Compare output" test, but fails each unit test.
    # print("2 + 2 = 4")
    # print("Unknown method: print_plus_2")
    # print("Secret string: \"abc\"")
    
    # After completing step 1:
    # Remove lines of code from step 1 and implement the call_method_named()
    # function above the main part of the program.
    call_method_named(printer, "print_2_plus_2")
    call_method_named(printer, "print_plus_2")
    call_method_named(printer, "print_secret")