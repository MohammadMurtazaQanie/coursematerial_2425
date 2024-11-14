def coins(amount):
    num_5_coins = amount // 5
    amount -= num_5_coins * 5

    num_2_coins = amount // 2
    amount -= num_2_coins * 2
    num_1_coins = amount
    return num_5_coins + num_2_coins + num_1_coins