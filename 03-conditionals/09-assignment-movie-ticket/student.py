# write your code here
import math

def movie_ticket(duration, imax, student, ticket_count):
    if duration <= 90:
        base = 10
    elif 90 < duration <= 120:
        base = 11
    elif 120 < duration <= 150:
        base = 12
    else:
        base = 15

    if student:
        base = base- 3
    if imax:
        base = math.ceil(base * 1.2)
    
    total_cost = base * ticket_count

    return total_cost