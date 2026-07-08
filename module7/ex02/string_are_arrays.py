#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none", end = "")
else:
    letter_z = False
    for caractere in sys.argv[1]:
        if caractere == "z":
            letter_z = True
            print(f"{caractere}", end = "")
    if letter_z == False:
        print("none", end = "")    
print()
