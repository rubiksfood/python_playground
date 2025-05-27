import re

with open("advent_of_code_23/day1/input.txt") as file:
    data = file.read().splitlines()
    def answer_1():
        running_total = 0
        for value in data:
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
        reg_ex = (r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
        running_total = 0
        for value in data:
            digit_list = re.findall(reg_ex, value)
            digit_one = digit_list[0]
            if digit_one.isdigit():
                num1 = digit_one
            else:
                for word in spelled:
                    if digit_one == word:
                        num1 = spelled.index(word) + 1
                        break
            digit_two = digit_list[-1]
            digit_two = str(digit_two)
            if digit_two.isdigit():
                num2 = digit_two
            else:
                for word in spelled:
                    if digit_two == word:
                        num2 = spelled.index(word) + 1
                        break
            combined = str(num1) + str(num2)
            combined = int(combined)
            running_total += combined
        print(running_total)
    answer_2()


    # The code below is an alternative approach that failed to work correctly.
    # It does not correctly handle when spelled digits were the last digit in the line.

    # def answer_2():
    #     spelled = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    #     running_total = 0
    #     for value in data:
    #         spelled_digit = ''
    #         digit_one = None
    #         for word in spelled:
    #             for char in value:
    #                 while digit_one is None:
    #                     if char.isdigit():
    #                         digit_one = char
    #                         break
    #                     else:
    #                         for i in range(len(word)):
    #                             if spelled_digit == word:
    #                                 digit_one = spelled.index(word) + 1
    #                                 break
    #                             elif char == word[i]:
    #                                 spelled_digit = spelled_digit + word[i]
    #                             else:
    #                                 spelled_digit = ''
    #                                 break

    #         value_reversed = value[::-1]
    #         spelled_digit_2 = ''
    #         digit_two = None
    #         for word in spelled:
    #             for char in value_reversed:
    #                 while digit_two is None:
    #                     if char.isdigit():
    #                         digit_two = char
    #                         break
    #                     else:
    #                         for i in range(len(word)):
    #                             if spelled_digit_2 == word:
    #                                 digit_two = spelled.index(word) + 1
    #                                 break
    #                             elif char == word[i]:
    #                                 spelled_digit_2 = spelled_digit_2 + word[i]
    #                             else:
    #                                 spelled_digit_2 = ''
    #                                 break
    #         combined = str(digit_one) + (digit_two)
    #         combined = int(combined)
    #         running_total += combined
    #     print(running_total)
    # answer_2()
