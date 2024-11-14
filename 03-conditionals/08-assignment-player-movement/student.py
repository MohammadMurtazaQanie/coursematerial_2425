# write your code here
def player_movement(position, left_arrow, right_arrow, shift):
    if shift == True:
        return movement * 2

    
    
    movement = 2 if shift else 1
    
    if left_arrow:
        return position - movement
    
    elif right_arrow:
        return position + movement
    
    return position