todos_deadlocks = set()

#deadlock de canto
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

#deadlock de duas caixas sem conseguir mexer
def deadlock_box(box,allboxes,obstacles):

    up = (box[0] ,box[1] - 1)
    down = (box[0], box[1] + 1)
    left = (box[0] - 1 , box[1])
    right = (box[0] + 1, box[1])

    for boxes in allboxes:
        if(up in obstacles and left in boxes or right in boxes):
            return True
        if(down in obstacles and left in boxes or right in boxes):
            return True
        if(left in obstacles and up in boxes or down in boxes):
            return True
        if(right in obstacles and up in boxes or down in boxes):
            return True
        else:
            return False