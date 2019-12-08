#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: December 2019
# This program calculates the biggest value in an array


import random


def calculate(number_array):
    # this function calculates the biggest value in a list

    # variables
    big_num = 0

    # process
    for counter in range(len(number_array)):
        if number_array[counter] > big_num:
            big_num = number_array[counter]

    return big_num


def main():
    # this function generates 10 random numbers and puts them in an array

    # array
    number_array = []

    # Adding numbers to an array
    for counter in range(10):
        random_num = random.randint(1, 100)
        print(random_num)
        number_array.append(random_num)

    # Process
    largest_number = calculate(number_array)

    # Output
    print("")
    print("The biggest number is {}" .format(largest_number))


if __name__ == "__main__":
    main()
