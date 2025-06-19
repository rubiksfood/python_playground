import re

with open("advent_of_code_23/day2/input.txt") as file:
    data = file.read().splitlines()
    def answer_1():
        running_total = 0
        for y in range(len(data)):
            for x in range(len(data[y])):
                if (data[y][x].isdigit()):
                    num_length = 1
                    while (x + num_length < len(data[y]) and data[y][x + num_length].isdigit()):
                        num_length += 1
                    num_candidate = int(data[y][x:x + num_length])

                    # Perhaps use RegEx to check for conditions - could shorten code

                    if ((data[y][x - 1] == '.' or data[y][x - 1].isdigit()) and (data[y][x + num_length] == '.' or data[y][x + num_length].isdigit())):
                        pass
                    else:
                        running_total += num_candidate
                        continue
                    
                    for i in range(-1, num_length + 1):
                        # if (y - 1 >= 0 and data[y - 1][x + i]  data[y - i][x].isdigit()): ...Find correct condition for checking values
                        if (data[y - 1][x + i] == '.' or data[y - 1][x + i].isdigit()): 
                            pass
                        else:
                            running_total += num_candidate
                            continue

                        if (data[y + 1][x + i] == '.' or data[y + 1][x + i].isdigit()): 
                            pass
                        else:
                            running_total += num_candidate
                            continue

        print(running_total)
        return running_total
    answer_1()