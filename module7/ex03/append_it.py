#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    for argument in sys.argv[1:]:
        if argument.find("ism") == -1:
            print(f"{argument}ism") 

# string.find(value, start, end)
# value:	Required. The value to search for
# start:	Optional. Where to start the search. Default is 0
# end:  	Optional. Where to end the search. Default is to the end of the string