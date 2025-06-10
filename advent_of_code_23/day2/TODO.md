# REMEMBER:
- Figure out the problem in your head first. LOOK OUT FOR EDGE-CASES!
- Then write pseudocode.
- THEN, write real code.

# Basis of Problem:
A random selection of cubes are revealed from a bag in 3 sets, i.e.
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
If a bag is filled with only 12 red cubes, 13 green cubes, and 14 blue cubes...

# Task:
Calculate the sum of the IDs of the games that were possible with the configuration.

# Mental solution:
- Assign the variables: red = 12, green = 13, blue = 14.
- Line by line, check each of the three sets - set by set.
- If any colours exceed the given variables, stop checking. Move to next line.
- Else, add the ID number to a running total.

# Pseudocode:

# Notes for solution:
- 4291: Answer is too high.
- 2545: Correct


## Part 2 - Task:
Calculate the sum of the powers of each colour of every game, with the least possible cubes.
I.e. If 1 games is possible with 2 red, 12 blue, 20 green = 2 x 12 x 20 = 480 += running total.

# Mental solution:
- Assign the variables: red = 0, green = 0, blue = 0.
- Line by line, check each of the three sets - set by set.
- If any colours in a set > the current colour variables, update them with the larger number.
- Multiply the final numbers of each colour at the end of each game.
- Add this number to the running total.

# Pseudocode:


# Notes for solution:

