with open("advent_of_code_23/day1/input.txt") as file:
    data = file.read().splitlines()
    def answer_1():
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