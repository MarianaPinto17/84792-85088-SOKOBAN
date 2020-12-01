
def deadlock_corner(box,obestacales):
    #calculate the neighbors of the next state box
    up = (box[0] ,box[1] - 1)
    down = (box[0], box[1] + 1)
    left = (box[0] - 1 , box[1])
    right = (box[0] + 1, box[1])
    if(up in obestacales and left in obestacales):
        print(up,left)
        return False
    elif(left in obestacales and down in obestacales):
        print(left,down)
        return False
    elif(down in obestacales and right in obestacales):
        print(down,right)
        return False
    elif(right in obestacales and up in obestacales):
        print(right,up)
        return False
    else:
        return True 