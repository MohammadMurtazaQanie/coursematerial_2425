# write your code here
def all_different(xs):
    for i in range(len(xs) -1):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs [j]:
                return False
    else:
        return True
    