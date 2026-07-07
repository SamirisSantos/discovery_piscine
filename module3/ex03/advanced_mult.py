#!/usr/bin/env python3
# for i in range(0, 11):
#     print(f"Table of {i} : ", end = "")
#     for j in range(0, 11):
#         print(i * j, end = " ")
#     print()

i = 0
while i <= 10:
    print(f"Table of {i} : ", end = "")
    j = 0
    while j <= 10:
        print(i * j, end = " ")
        j += 1
    i += 1
    print()