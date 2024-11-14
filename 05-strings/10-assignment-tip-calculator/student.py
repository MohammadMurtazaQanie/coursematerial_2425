# write your code here

def tip_calculator():
    total_price = float(input("Enter total price: ")) 
    percent = input("Enter tip percentage (default=20): ")
    
    if percent == '':
        tip = 20  
    else: 
        tip = int(percent)

    total = total_price + (total_price * tip / 100) 
    print(f"You have to pay {round(total)}")  