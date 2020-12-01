todos_deadlocks = set()

def deadlock_corner(box,obstacles):
    #calculate the neighbors of the next state box
    global todos_deadlocks
    up = (box[0] ,box[1] - 1)
    down = (box[0], box[1] + 1)
    left = (box[0] - 1 , box[1])
    right = (box[0] + 1, box[1])
    if(up in obstacles and left in obstacles):
        todos_deadlocks.add(box)
        print(up,left)
        return True
    elif(left in obstacles and down in obstacles):
        todos_deadlocks.add(box)
        print(left,down)
        return True
    elif(down in obstacles and right in obstacles):
        todos_deadlocks.add(box)
        print(down,right)
        return True
    elif(right in obstacles and up in obstacles):
        todos_deadlocks.add(box)
        print(right,up)
        return True
    else:
        return False 