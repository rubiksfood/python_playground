import re

with open("advent_of_code_23/day3/input.txt") as file:
    data = file.read().splitlines()
    def answer_1():
        symbols = [',', '!', '?', ':', ';', '-', '_', '=', '+', '*', '/', '\\', '|', '(', ')', '[', ']', '{', '}', '<', '>', '"', "'", '@', '#', '$', '%', '^', '&', '~', '`']
        running_total = 0
        for y in range(len(data)):
            for x in range(len(data[y])):
                if (data[y][x].isdigit()):
                    # Check if the previous character is a digit, if so, skip
                    if (x - 1 >= 0 and data[y][x - 1].isdigit()):
                        continue

                    num_length = 1
                    while (x + num_length < len(data[y]) and data[y][x + num_length].isdigit()):
                        num_length += 1
                    num_candidate = int(data[y][x:x + num_length])

                    if (x - 1 >= 0):
                        if (any(symbol in data[y][x - 1] for symbol in symbols)):
                            running_total += num_candidate
                            continue

                    if (x + num_length < len(data[y])):
                        if (any(symbol in data[y][x + num_length] for symbol in symbols)):
                            running_total += num_candidate
                            continue
                    
                    for i in range(-1, num_length + 1):
                        if (y - 1 >= 0 and x + i < len(data[y]) and x + i >= 0): 
                            if (any(symbol in data[y - 1][x + i] for symbol in symbols)):
                                running_total += num_candidate
                                continue

                        if (y + 1 < len(data) and x + i < len(data[y]) and x + i >= 0): 
                            if (any(symbol in data[y + 1][x + i] for symbol in symbols)):
                                running_total += num_candidate
                                continue

        print(running_total)
        return running_total
    answer_1()