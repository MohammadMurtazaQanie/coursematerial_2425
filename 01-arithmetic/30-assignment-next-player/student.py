def next_player(player, player_count):
    something = (player + 1) % player_count 
    return something

print(next_player(8,10))