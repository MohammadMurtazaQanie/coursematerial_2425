# write your code here
def is_student_id(string): 
    if (len(string) == 8) and (string[0] == "r" or "s" or "R" or "S") and (string[1:]==int):
        return True
    else:
        return False