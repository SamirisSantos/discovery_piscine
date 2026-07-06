#!/usr/bin/env python3

first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the second number:"))
res = first_number * second_number

if res > 0:
    print(f"{first_number} x {second_number} = {res}")
    print("The result is positive.")
elif res < 0:
    print(f"{first_number} x {second_number} = {res}")
    print("The result is negative.")
else:
    print(f"{first_number} x {second_number} = {res}")
    print("The result is positive and negative.")

# print("{} x {} = {}".format(first_number, second_number, res))
# print("{num1} x {num2} = {resultado}".format(num1=first_number, num2=second_number, resultado=res))
# print(first_number, "x", second_number, "=", res)
