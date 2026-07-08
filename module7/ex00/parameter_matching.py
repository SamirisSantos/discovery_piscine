#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    world = input("What was the parameter? ")
    if sys.argv[1] == world:
        print("Good Job!")
    else:
        print("Nope, sorry")