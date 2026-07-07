#!/usr/bin/env python3
import sys

if len(sys.argv) < 3:
    print("none")
else:
    len = len(sys.argv)
    for i in range(len - 1, 0, -1):
        print(sys.argv[i])

# range(inicio, fim, passo)