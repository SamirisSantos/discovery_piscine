#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    scan = sys.argv[1]
    text = sys.argv[2]
    result = re.findall(scan, text)
    print(len(result))
