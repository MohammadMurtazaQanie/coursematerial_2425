# write your code here
def subtuple(xs, ys):
    if not ys:
        return True
    for i in range(len(xs)- len(ys)+1):
        if xs[i:i+len(ys)] == ys:
            return True
    else:
        False