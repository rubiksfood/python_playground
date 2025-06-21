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

    def answer_2():
        running_total = 0
        for y in range(len(data)):
            for x in range(len(data[y])):
                if (data[y][x] == '*'):
                    num_list = []

                    if (x - 1 >= 0 and data[y][x - 1].isdigit()):
                        leftmost = x - 1
                        while (leftmost - 1 >= 0 and data[y][leftmost - 1].isdigit()):
                            leftmost -= 1
                        if (num_list and num_list[-1] == int(data[y][leftmost:x])):
                            continue
                        num_list.append(int(data[y][leftmost:x]))

                    if (x + 1 < len(data[y]) and data[y][x + 1].isdigit()):
                        rightmost = x + 1
                        while (rightmost + 1 < len(data[y]) and data[y][rightmost + 1].isdigit()):
                            rightmost += 1
                        if (num_list and num_list[-1] == int(data[y][x + 1:rightmost + 1])):
                            continue
                        num_list.append(int(data[y][x + 1:rightmost + 1]))

                    for i in range(-1, 2):
                        if (y - 1 >= 0 and x + i < len(data[y - 1]) and x + i >= 0):
                            if (data[y - 1][x + i].isdigit()):
                                leftmost = x + i
                                rightmost = x + i

                                while (leftmost - 1 >= 0 and data[y - 1][leftmost - 1].isdigit()):
                                    leftmost -= 1
                                while (rightmost + 1 < len(data[y - 1]) and data[y - 1][rightmost + 1].isdigit()):
                                    rightmost += 1
                                if (num_list and num_list[-1] == int(data[y - 1][leftmost:rightmost + 1])):
                                    continue
                                num_list.append(int(data[y - 1][leftmost:rightmost + 1]))
                                
                    for i in range(-1, 2):
                        if (y + 1 < len(data[y + 1]) and x + i < len(data[y + 1]) and x + i >= 0):
                            if (data[y + 1][x + i].isdigit()):
                                leftmost = x + i
                                rightmost = x + i

                                while (leftmost - 1 >= 0 and data[y + 1][leftmost - 1].isdigit()):
                                    leftmost -= 1
                                while (rightmost + 1 < len(data[y + 1]) and data[y + 1][rightmost + 1].isdigit()):
                                    rightmost += 1
                                if (num_list and num_list[-1] == int(data[y + 1][leftmost:rightmost + 1])):
                                    continue
                                num_list.append(int(data[y + 1][leftmost:rightmost + 1]))

                    if (len(num_list) == 2):
                        running_total += num_list[0] * num_list[1]
                        continue
                    
        print(running_total)
    answer_2()