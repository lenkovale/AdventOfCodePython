from math import prod 

def compute_games(document):
    result = 0
    for line in document.splitlines():
        game_numbers = line.split(":") # ["game 1", "8 red, 6 blue, 7 green; 2 red"]
        game_rounds = game_numbers[1].split(";") # ["8 red, 6 blue, 7 green", "2 red"]
        max_colors = {"red": 0, "blue": 0, "green": 0}
        for game_round in game_rounds:
            color_sets = game_round.split(",") # color_sets = ["8 red", "6 blue", "7 green"]
            for one_color in color_sets: # one_color = "8 red"
                num_color = one_color.split() # ["8", "red"]
                if max_colors[num_color[1]] < int(num_color[0]):
                    max_colors[num_color[1]] = int(num_color[0])
        result += (prod(max_colors.values()))
    return result
            
