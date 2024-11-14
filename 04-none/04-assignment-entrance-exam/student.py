def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    skip  = 0
    taken  = 0
    total = 0

    if grade1 is None:
        skip  = skip + 1
    else: 
        taken =  taken + 1
        total = total + grade1

    if grade2 is None:
        skip  = skip + 1
    else: 
        taken =  taken + 1
        total = total + grade2
    
    if grade3 is None:
        skip  = skip + 1
    else: 
        taken =  taken + 1
        total = total + grade3

    if grade4 is None:
        skip  = skip + 1
    else: 
        taken =  taken + 1
        total = total + grade4

    if grade5 is None:
        skip  = skip + 1
    else: 
        taken =  taken + 1
        total = total + grade5
    if skip > 1:
        return False 

    if (total/taken >= 12) and taken >0 : 
        return True
    else:
        return False