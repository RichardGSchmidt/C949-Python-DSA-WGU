#    8.8 LAB: All permutations of names
#   
#   Write a program that lists all ways people can line up for a photo (all permutations of a list of strings). The program will read a list of one word names, then use a recursive function to create and output all possible orderings of those names separated by a comma, one ordering per line.
#   
#   When the input is:
#   
#   Julia Lucas Mia
#   
#   then the output is (must match the below ordering):
#   
#   Julia, Lucas, Mia 
#   Julia, Mia, Lucas
#   Lucas, Julia, Mia
#   Lucas, Mia, Julia
#   Mia, Julia, Lucas
#   Mia, Lucas, Julia

# Solution:

def print_all_permutations(permList, nameList):
    # Varible Declaration block.
    nameCopy = nameList[:]
    permCopy = permList[:]
    
    # base case, prints the list
    if (len(nameCopy)==0):
        #string builder function
        out_str = ''
        for i in range(len(permCopy)):
            if i == 0:
                out_str += permCopy[i]
            else:
                out_str += f', {permCopy[i]}'
        print(f'{out_str}')
    
    # recursive case, itterates through the list making recursive calls
    #   until the base case is reached (len(nameCopy)==0)
    else:
        for i, name in enumerate(nameCopy):
            # extra copies declared / reset here to avoid altering the list
            #   for the next itteration of the loop
            nameOut = nameCopy[:]
            permOut = permCopy[:]

            # add the name to the permutation list
            permOut.append(nameOut[i])
            
            # remove the name from the name list
            nameOut.pop(i)
            
            # recursive call
            print_all_permutations(permOut, nameOut)
# End solution

if __name__ == "__main__": 
    nameList = input().split(' ')
    permList = []
    print_all_permutations(permList, nameList)