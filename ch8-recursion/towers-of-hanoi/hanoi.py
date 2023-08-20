#   Towers of Hanoi
#   A good example of recursion
#   Adapted from MITopencourseware
#   Shows up in job interviews

# print handler function
def printmove(fr, to):
    print(f'Move {fr} to {to}.')

# posts are numbered 1, 2, and 3 by default with target of 2

def hanoi(towersize, fr=1, to=2, spare=3):

    # base case, if only one piece is in the stack to be moved
    if towersize == 1:
        printmove(fr,to)

    
    # recursive calls. moves everything but to bottom to a spare, then moves
    # then bottom to the target, everything but the bottom from the spare
    # to the target.
    else:
        # move all but one piece in the stack (the bottom) to the spare post
        hanoi(towersize-1, fr, spare, to)

        # move the bottom to the target post
        hanoi(1, fr, to, spare)

        # move the stack on the spare post to the target post
        hanoi(towersize-1, spare, to, fr)

hanoi(5)