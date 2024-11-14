def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    
    cakes_eggs = eggs // eggs_per_cake
    cakes_flour = flour // flour_per_cake
    cakes_butter = butter // butter_per_cake
    cakes_sugar = sugar // sugar_per_cake
    return min(cakes_eggs, cakes_flour, cakes_butter, cakes_sugar)