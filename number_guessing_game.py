#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program is number guessing game

import constants


def main():
    # this function checks if number is not 5

    # input
    your_number = int(input("Enter your number "))
    print("")

    # process
    if your_number > constants.MY_NUMBER:
        # output
        print("You are wrong")


if __name__ == "__main__":
    main()
