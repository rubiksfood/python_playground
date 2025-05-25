import re

with open("advent_of_code_23/day1/test_input.txt") as file:
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
        reg_ex = (r'one|two|three|four|five|six|seven|eight|nine|(\d)')
        running_total = 0
        num1 = 0
        num2 = 0
        for value in data:
            digit_one = re.search(reg_ex, value)
            if digit_one[0].isdigit():
                num1 = digit_one[0]
            else:
                for word in spelled:
                    if digit_one[0] == word:
                        num1 = spelled.index(word) + 1
                        break
            digit_two = digit_one.end(1)
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
            print(combined)
            running_total += combined
        print(running_total)
    answer_2()

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
    #                             elif char == i:
    #                                 spelled_digit = spelled_digit + word[i]
    #                             else:
    #                                 spelled_digit = ''
    #                                 break

    #         value_reversed = value[::-1]
    #         spelled_digit_2 = ''
    #         digit_two = None
    #         while digit_two is None:
    #             # The below code has not been updated to use new logic from above
    #             for word in spelled:
    #                 word_reversed = word[::-1]
    #                 for letter in word_reversed:
    #                     for char_2 in value_reversed:
    #                         if char_2.isdigit():
    #                             digit_two = char_2
    #                             break
    #                         else:
    #                             if spelled_digit_2 == word:
    #                                 digit_two = spelled.index(word) + 1
    #                                 break
    #                             elif char == letter:
    #                                 spelled_digit_2 += char
    #                             else:
    #                                 spelled_digit_2 = ''
    #                                 break
    #         combined = str(digit_one) + (digit_two)
    #         combined = int(combined)
    #         running_total += combined
    #     print(running_total)
    # answer_2()


    # def answer_2():
    #     spelled = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    #     running_total = 0
    #     for value in data:
    #         digit_one = None
    #         spelled_digit = ''
    #         for char in value:
    #             if char.isdigit():
    #                 digit_one = char
    #                 break
    #             else:
    #                 for word in spelled:
    #                     for letter in word:
    #                         if spelled_digit == word:
    #                             digit_one = spelled.index(word) + 1
    #                             break
    #                         elif char == letter:
    #                             # This is where the error occurs
    #                             # spelled_digit = ''
    #                             # for i in range(len(spelled)):
    #                             #     for j in range(len(spelled[i])):
    #                             #         if char == spelled[i][j]:
    #                             #             spelled_digit += char
    #                             #         else:
    #                             #             break
    #                             #         if spelled_digit == spelled[i]:
    #                             #             digit_one = i + 1
    #                             #             break
    #                             spelled_digit += char
    #                             continue
    #                         else:
    #                             spelled_digit = ''
    #                             break
    #         value_reversed = value[::-1]

    #         digit_two = None
    #         spelled_digit = ''
    #         for char_2 in value_reversed:
    #             if char_2.isdigit():
    #                 digit_two = char_2
    #                 break
    #             else:
    #                 spelled_digit_2 = ''
    #                 for word in spelled:
    #                     word_reversed = word[::-1]
    #                     for letter in word_reversed:
    #                         if spelled_digit_2 == word:
    #                             digit_two = spelled.index(word) + 1
    #                             break
    #                         elif char == letter:
    #                             spelled_digit_2 += char
    #                         else:
    #                             spelled_digit_2 = ''
    #                             break
    #         combined = str(digit_one) + (digit_two)
    #         combined = int(combined)
    #         running_total += combined
    #     print(running_total)
    # answer_2()

    # def answer_2():
    #     spelled = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    #     running_total = 0
    #     for value in data:
    #         digit_one = None
    #         digit_two = None
    #         for char_2 in value:
    #             if char_2.isdigit():
    #                 digit_one = char_2
    #                 break
    #             else:
    #                 spelled_digit = ''
    #                 for word in spelled:
    #                     for letter in word:
    #                         if char_2 == letter:
    #                             spelled_digit += char_2
    #                         else:
    #                             break
    #                         if spelled_digit == word:
    #                             digit_one = i + 1
    #                             break
    #         valueReverse = value[::-1]
    #         for char_2 in valueReverse:
    #             if char_2.isdigit():
    #                 digit_two = char_2
    #                 break
    #             else:
    #                 spelled_digit_2 = ''
    #                 for i in range(0):
    #                     for j in range(len(spelled[i]), -1, -1):
    #                         if char_2 == spelled[i][j]:
    #                             spelled_digit_2 += char_2
    #                         else:
    #                             break
    #                         if spelled_digit_2 == spelled[i]:
    #                             digit_two = i + 1
    #                             break
    #         combined = str(digit_one) + (digit_two)
    #         combined = int(combined)
    #         running_total += combined
    #     print(running_total)
    # answer_2()

    