# write your code here
def box(string):
    first_line = "+" + "-" * (len(string) + 2) + "+\n"  
    second_line = f"| {string} |\n"  
    third_line = "+" + "-" * (len(string) + 2) + "+"  
    
    return first_line + second_line + third_line