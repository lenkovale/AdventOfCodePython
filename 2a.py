def compute_games(document):
    result = 0
    rules = {"red": 12, "blue": 14, "green": 13}
    for line in document.splitlines():
        game_numbers = line.split(":") # ["game 1", "8 red, 6 blue, 7 green; 2 red"]
        game_id = int(game_numbers[0][4:])
        game_rounds = game_numbers[1].split(";") # ["8 red, 6 blue, 7 green", "2 red"]
        is_valid = True
        for game_round in game_rounds:
            color_sets = game_round.split(",") # color_sets = ["8 red", "6 blue", "7 green"]
            for one_color in color_sets: # one_color = "8 red"
                num_color = one_color.split() # ["8", "red"]
                if rules[num_color[1]] < int(num_color[0]):
                    is_valid = False
        if is_valid:
            result += game_id
    return result

