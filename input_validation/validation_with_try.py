"""
Program validation_with_try.py

Author: Greg Wilhelm

Last date modified: 2/14/2020

The purpose of this program is to prompt the user for their first name, last name, age, and three scores and then
calculate the average of their three scores via a function call. What the user entered and the average of their scores
is then printed at the end. Modified to catch an exception where a negative value is entered for a score.

"""

NUMBER_TESTS = 3


def average(score1, score2, score3):
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    else:
        return float((score1 + score2 + score3) / NUMBER_TESTS)


if __name__ == '__main__':

    try:
        first_name = input("Please enter your first name: ")
        last_name = input("Please is your last name: ")
        age = input("Please enter your age: ")
        score_1_input = int(input("Please enter a score out of 100: "))
        score_2_input = int(input("Please enter another score out of 100: "))
        score_3_input = int(input("Please enter another score out of 100: "))

        average_grade = average(score_1_input, score_2_input, score_3_input)

        print(f"{last_name}, {first_name} age: {age} average grade: {average_grade:.2f}")
    except ValueError:
        print("A negative value cannot be entered for a score.")

# Input:            Greg, Wilhelm, 35, 90, 89, 77
# Expected Output:  "Wilhelm, Greg age: 35 average grade: 85.33"
# Actual Output:    "Wilhelm, Greg age: 35 average grade: 85.33"
#
# Input:            Tony, Stark, 49, 100, 100, 100
# Expected Output:  "Stark, Tony age: 49 average grade: 100.00"
# Actual Output:    "Stark, Tony age: 49 average grade: 100.00"
#
# Input:            Bruce, Banner, 50, 16, 100, 0
# Expected Output:  "Banner, Bruce age: 50 average grade: 38.67"
# Actual Output:    "Banner, Bruce age: 50 average grade: 38.67"
