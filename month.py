#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 13 2022
# This program asks the user for a integer between 1 and 12 it thens corresponds a month to that value


def find_month(month):
    # Get the the integer from the user
    months = {
        1: "{} represents January.".format(month),
        2: "{} represents February.".format(month),
        3: "{} represents March.".format(month),
        4: "{} represents April.".format(month),
        5: "{} represents May.".format(month),
        6: "{} represents June.".format(month),
        7: "{} represents July.".format(month),
        8: "{} represents August.".format(month),
        9: "{} represents September.".format(month),
        10: "{} represents October.".format(month),
        11: "{} represents November.".format(month),
        12: "{} represents December.".format(month),
    }
    return months.get(month, "Error. {} does not represent a month.".format(month))


if __name__ == "__main__":
    user_month = int(input("Enter a integer between 1-12: "))

    print(find_month(user_month))
