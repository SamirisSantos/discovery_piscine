#!/usr/bin/env python3
import sys

def downcase_it(argument):
    if len(sys.argv) == 1:
        print("none")
    else:
        for arg in argument[1:]:
            print(f"{arg.lower()}")

downcase_it(sys.argv)
