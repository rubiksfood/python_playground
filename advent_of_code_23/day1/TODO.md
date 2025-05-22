# REMEMBER:
- Figure out the problem in your head first.
- Then write pseudocode.
- THEN, write real code.

# Basis of Problem:
The target value of each line can be found by combining the first digit with the last digit to form a two-digit number.
If there is only one digit, that is both the first & the last digit.

For example:

2def1       = 21
lpl3rew8poq = 38
g1h2o3s4t7s = 17
pleb6ucher  = 66
= 142

# Task:
Calculate the sum of all the values.

# Mental solution:
Read in the input line by line.
Check for the first number in a line.
Check for the last number in a line.
Concatenate the 2 numbers.
Turn the 2-digit number into an int.
Add the new int to a running total.

# Pseudocode:

with open("advent_of_code_23/day1/input.txt") as file:
    data = file.read().splitlines()
    def answer_1:
        running_total = 0
        for value in data:
            digit_one = None
            digit_two = None
            for char in value:
                if char.isdigit():
                    digit_one = char
                    break

# Real code:

with open("advent_of_code_23/day1/input.txt") as file:
    data = file.read().splitlines()
    def answer_1:
        running_total = 0
        for value in data:
            digit_one = None
            digit_two = None
            for char in value:
                if char.isdigit():
                    digit_one = char
                    break
            valueReverse = value[::-1]
            for char in valueReverse:
                if char.isdigit():
                    digit_two = char
                    break
            combined = digit_one + digit_two
            combined = int(combined)
            running_total += combined
        print(running_total)
    answer_1()

 def answer_2():
        spelled = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
        running_total = 0
        for value in data:
            digit_one = None
            digit_two = None
            for char in value:
                if char.isdigit():
                    digit_one = char
                    break
                else:
                    for i in range(0):
                        for j in range(0):
                            if char == spelled[i][j]:
                                spelled_digit += char
                            if spelled_digit == spelled[i]:
                                digit_one = i + 1
                                break
            valueReverse = value[::-1]
            for char in valueReverse:
                if char.isdigit():
                    digit_two = char
                    break
                else: 
                    for i in range(0):
                        for j in range(0):
                            if char == spelled[i][j]:
                                spelled_digit_2 += char
                            if spelled_digit_2 == spelled[i]:
                                digit_two = i + 1
                                break
            combined = digit_one + digit_two
            combined = int(combined)
            running_total += combined
        print(running_total)
    answer_2()
