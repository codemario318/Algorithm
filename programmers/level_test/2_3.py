board = [[0,1,1,1]
        ,[1,1,1,1]
        ,[1,1,1,1]
        ,[0,0,1,0]]

board = [[0,0,1,1]
        ,[1,1,1,1]
        ,[0,0,0,0]]

import numpy as np
arr = np.array(board)
hight = len(board)
width = len(board[0])

size = width if width < hight else hight
x,y = 0,0

while size > 0:
    print(x,y)
    print(arr[x:x+size,y:y+size])
    if sum(arr[x:x+size,y:y+size].flatten()) == size **2:
        print(size**2)
        break
    if y+size < width:
        y+= 1
    elif y+size == width:
        x += 1
        y = 0
    if x+size > hight:
        x=0
        y=0
        size -= 1
###############################################################################################
import numpy as np
def soultion(board):
    arr = np.array(board)
    hight = len(board)
    width = len(board[0])

    size = width if width < hight else hight
    x,y = 0,0

    while size > 0:
        if sum(arr[x:x+size,y:y+size].flatten()) == size **2:
            return size**2
        if y+size < width:
            y+= 1
        elif y+size == width:
            x += 1
            y = 0
        if x+size > hight:
            x=0
            y=0
            size -= 1
    return 0
