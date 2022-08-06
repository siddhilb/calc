#! /usr/bin/env python3

# Filename: math.py
# Author: Siddhi
#print('')
division = False
multiply = False
add = False
subtract = False
while True:
    operation = input('What operation? A for addition, S for subtraction, M for multiplication, and D for division. Q to quit. ')
    operation = operation.lower()
    if operation == 'q':
        break
    first = float(input('Input the first number! ',))
    second = float(input('Input the second number! ',))
    if operation == 'a':
        answer = first + second
        print(first,'+',second,'is',answer) 
    if operation == 'm':
        answer = first * second
        print(first,'x',second,'is:',answer) 
    if operation == 'd':
        answer = first / second
        print(first,'÷',second,'is:',answer) 
    if operation == 's':
        answer = first - second
        print(first,'-',second,'is:',answer) 

