# write your code here
def sum_input():
    total = 0
    while True:
        number = int(input("Enter integer: "))
        if number == 0:
            break
        total += number
    print(f"The sum equals {total}.")