import os
first1 = input("path1: ")
second2 = input("path1: ")
with open('first1', 'r') as firstfile, open('second2', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)