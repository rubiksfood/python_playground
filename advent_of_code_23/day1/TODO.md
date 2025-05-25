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

# Mental solution (p.2):
- Read in the input, line by line.
- Using RegEx, search for the 1st spelled number or digit. Assign to digit_one.
- Using RegEx, search for the last spelled number or digit. Assign to digit_two.
- Concatenate the 2 numbers.
- Turn the 2-digit number into an int.
- Add the new int to a running total.

# Notes for solution:
- Using RegEx to find the last instance of a pattern?
Use { .find() / re.search() & .rfind()??? }

# Pseudocode (p.2):
