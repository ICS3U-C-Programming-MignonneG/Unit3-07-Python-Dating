#!/usr/bin/env python3

# Created by: Mignonne Gihozo
# Created on: October 26 2026
# This program checks whether the user is eligible to date the grandchild


def main():
    # this function checks whether the user is eligible to date the grandchild

    # input
    age_as_string = input("Enter your age: ")
    print("")

    # process & output
    try:
        age = int(age_as_string)
        # Check if the number is invalid (negative) or unrealistically high using a logical OR operator
        if age < 0 or age > 120:
            print("{} is not a valid number!".format(age_as_string))
        elif age >= 25 and age <= 40:
            print("You can date my grandchild!")
        else:
            print("You are not eligible to date my grandchild!")
    except ValueError:
        print("{} is not a valid integer!".format(age_as_string))
    finally:
        print("Thank you for playing this game!")


if __name__ == "__main__":
    main()
