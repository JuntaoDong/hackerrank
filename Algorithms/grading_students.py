#!/bin/python3

import os
import sys

def gradingStudents(grades):
    final = []
    for g in grades:
        if g < 38:
            final.append(g)
        elif g % 5 == 3:
            final.append(g+2)
        elif g % 5 == 4:
            final.append(g+1)
        else:
            final.append(g)
    return(final)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
