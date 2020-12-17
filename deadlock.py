todos_cantos = set()

#deadlock de canto
def deadlock_corner(box,obstacles):
    #calculate the neighbors of the next state box
    global todos_cantos
    up = (box[0] ,box[1] - 1)
    down = (box[0], box[1] + 1)
    left = (box[0] - 1 , box[1])
    right = (box[0] + 1, box[1])
    if(up in obstacles and left in obstacles):
        todos_cantos.add(box)
        #print(up,left)
        return True
    elif(left in obstacles and down in obstacles):
        todos_cantos.add(box)
        #print(left,down)
        return True
    elif(down in obstacles and right in obstacles):
        todos_cantos.add(box)
        #print(down,right)
        return True
    elif(right in obstacles and up in obstacles):
        todos_cantos.add(box)
        #print(right,up)
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
        elif(down in obstacles and left in boxes or right in boxes):
            return True
        elif(left in obstacles and up in boxes or down in boxes):
            return True
        elif(right in obstacles and up in boxes or down in boxes):
            return True
        else:
            return False

def isWall(position,x,y,corner,obstacles):
    new_position = position

    up = (new_position[0] ,new_position[1] - 1)
    down = (new_position[0], new_position[1] + 1)
    left = (new_position[0] - 1 , new_position[1])
    right = (new_position[0] + 1, new_position[1])

    #Enquanto nova posição não é corner
    while new_position != corner:
        if down in obstacles and x>0 and y>0:
            new_position = (new_position[0]+x, new_position[1]+y)        
        else:
            return False
    return True

def deadlock_boxnotgoal(box,goals,obstacles):
    up = (box[0] ,box[1] - 1)
    down = (box[0], box[1] + 1)
    left = (box[0] - 1 , box[1])
    right = (box[0] + 1, box[1])
   
    #se em baixo da caixa está parede
    if down in obstacles:
        # para cada canto existente no mapa
        for goal in goals:
            for corner in todos_cantos:
            # se o canto tem o mesmo y que a box estão ao mesmo nível
                if corner[1] == box[1] and goal[1] != box[1]:
                    isWall(box,1,0,corner,obstacles)
                    isWall(box,-1,0,corner,obstacles)
                else:
                    return None
    else:
        return False
