# write your code here
def heatwave(temperatures):
   
    consecutive_25 = 0
    consecutive_30 = 0
    for temp in temperatures:
        if temp >= 25:
            consecutive_25 += 1
            if temp >= 30:
                consecutive_30 += 1
        else:
            consecutive_25 = 0
            consecutive_30 = 0
       
        if consecutive_25 >= 5 and consecutive_30 >= 3:
            return True

    return False