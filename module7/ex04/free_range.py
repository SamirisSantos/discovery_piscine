#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
elif sys.argv[1] > sys.argv[2]:
    print("The second number smaller than the second first")
else:
    number = []
    number.extend(range(int(sys.argv[1]),(int(sys.argv[2])) + 1))
    print(number)