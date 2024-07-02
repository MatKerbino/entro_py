import sys


def add(a, b):
    answer = a + b
    print(str(a) + " + " + str (b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str (b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " x " + str (b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str (b) + " = " + str(answer))

print("A. Addiction")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

choice = input("CHOSE YOUR FATE ")

if choice == 'a' or choice == 'A':
    print("Addiction")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    add(a, b)
if choice == 'b' or choice == 'B':
    print("Subtraction")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    sub(a, b)
if choice == 'c' or choice == 'C':
    print("Multiplication")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    mul(a, b)
if choice == 'd' or choice == 'D':
    print("Division")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    div(a, b)
else:
    quit()