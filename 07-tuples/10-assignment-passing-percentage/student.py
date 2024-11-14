# write your code here

def passing_percentage(grades): 
    p = 0
    if not grades:
        return 0 
    
    for i in grades:
        if i >=  10:
            p = p + 1
    total =  len(grades)
    percentage = (p/total) * 100
    return percentage