"""Exercise 1: Extract Function"""

import math


def get_grades(n_student):
    grade_list = []
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list


def calculate_mean(grade_list):
    total = 0
    for grade in grade_list:
        total += grade
    return total / len(grade_list)


def calculate_sd(grade_list, mean):
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    return math.sqrt(sum_of_sqrs / len(grade_list))


def print_grades(mean, sd):
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


def main():
    # Get the inputs from the user
    grade_list = get_grades(5)

    # Calculate the mean and standard deviation of the grades
    mean = calculate_mean(grade_list)

    # Calculate standard deviation
    sd = calculate_sd(grade_list, mean)

    # Print out the mean and standard deviation in a nice format.
    print_grades(mean, sd)


main()
