#! /usr/bin/env python3

# Filename: add.py
# Author: Siddhi
#print('')
division = False
multiply = False
add = False
subtract = False
operation = input('What operation? A for addition, s for subtraction, m for multiplication, and d for division. ')
print("Type 'stop' to stop the program.")
if operation == 'a' or operation == 's' or operation== 'd' or operation == 'm':
    first = int(input('Input the first number! ',))
#print('')
    second = int(input('Input the second number! ',))
#print('')
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
if operation == 'stop':
    quit()
operation = input('What operation? A for addition, s for subtraction, m for multiplication, and d for division. ',)
