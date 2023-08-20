#   Towers of Hanoi
#   Good example of recursion
#   Shows up in job interviews


#posts are numbered 1, 2, and 3


def printmove(fr, to):
    print(f'Move {fr} to {to}.')

def hanoi(towersize, fr, to, spare):
    if towersize == 1:
        printmove(fr,to)
    else:
        hanoi(towersize-1, fr, spare, to)
        hanoi(1, fr, to, spare)
        hanoi(towersize-1, spare, to, fr)


hanoi( 5,1,2,3 )