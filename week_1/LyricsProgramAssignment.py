# Instructors: Tarun Kumar & Bahawal Baloch
# Developer: Zaid Ahmed Soomro
# Institute: MUET Jamshoro
# Department: Software Engineering (First Semester)
# Language: Python
# DSU-DSC Python Bootcamp 2020
# Date: 9/12/2020 Wednesday

import time


def foo(take_input):
    lyrics = take_input.split(', ')
    for line in lyrics:
        print("\n\t" + line)
        time.sleep(1)


# Please add a comma (, )  where you want to end each line
foo("Twinkle Twinkle little star, How I wonder what you are, Up above the world so high, Like a diamond in the sky")
