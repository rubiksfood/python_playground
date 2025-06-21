# REMEMBER:
- Figure out the problem in your head first. LOOK OUT FOR EDGE-CASES!
- Then write pseudocode.
- THEN, write real code.

# Basis of Problem:
You have several scratch cards. 

Each card has two lists of numbers separated by a vertical bar '|': a list of winning numbers and then a list of numbers you have.
The first match makes the card worth one point - each match after the first doubles the point value of that card.

# Task:
How many points are all the cards worth in total?


# Mental solution:

Note: Cards with winning numbers have points equal to a power of 2. 
I.e. 1, 2, 4, 8, 16...

- Look at each line in the input.
- Ignore everything before the ':'
- Separate the winning numbers from the player numbers. winning_nums / player_nums
- Check for each of the player nums if they are in the winning nums.
- If a player_num is in winning_nums, count += 1.
- After counting all the winning_nums for a card, calculate 2 to the power of the 'count'
- Add that value to the running_total.

# Pseudocode:


# Notes for solution:



## Part 2 - Task:


# Mental solution:
- 

# Pseudocode:


# Notes for solution:

