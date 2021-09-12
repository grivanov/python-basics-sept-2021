from math import *


figure = input()

if figure == "square" or figure == "circle":
    num1 = float(input())
else:
    num1 = float(input())
    num2 = float(input())

if figure == "square":
    result = num1 * num1
elif figure == "circle":
    result = pi * (num1 * num1)
elif figure == "rectangle":
    result = num1 * num2
else:
    result = (num1 * num2) / 2

print(f"{result:.3f}")
