# write your code here
def earlier(h1, m1, h2, m2):
    if h1 < h2:
        return True
    elif h1 == h2 and m1 < m2:
        return True
    else:
        return False