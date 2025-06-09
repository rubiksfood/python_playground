import re

with open("advent_of_code_23/day2/input.txt") as file:
    data = file.read().splitlines()
    RED = 12
    GREEN = 13
    BLUE = 14
    running_total = 0

    id_regex = r'Game (\d+)'
    red_regex = r'(\d+) red'
    green_regex = r'(\d+) green'
    blue_regex = r'(\d+) blue'

    for game in data:
        invalid_game = False
        while invalid_game == False:
            id = re.search(id_regex, game).group(1)
            # print('id = ' + id)

            sets = game.split(";")
            # print('sets = ' + str(sets))

            for set in sets:
                red_in_set = re.search(red_regex, set)
                green_in_set = re.search(green_regex, set)
                blue_in_set = re.search(blue_regex, set)

                if (red_in_set and int(red_in_set.group(1)) > RED) or (green_in_set and int(green_in_set.group(1)) > GREEN) or (blue_in_set and int(blue_in_set.group(1)) > BLUE):
                    # print('Invalid game: ' + id)
                    invalid_game = True
                    break
            
            if not invalid_game:
                running_total += int(id)
                invalid_game = True
        # print('running_total = ' + str(running_total))

    print('Final total = ' + str(running_total))