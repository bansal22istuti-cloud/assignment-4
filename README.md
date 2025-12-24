## Assignment-4
this repository contains two task each for the assignment 4 of tutedude python program

## Task 1
this task aims
Program of task 1
ass3task1.py

def factorial(n): if n==1: return 1 else: return n*factorial(n-1)

num=int(input("enter your number: ")) result=factorial(num) print(f"the factorial of {num} is {result}") input('press enter to exit')

Explanation of task 1 program
here a fuction named factorial is user defined that take a number as an argument. here while defining the function with the help of if else statement, the condition provides both a base condition for the recursion to end that being once the number becoming one to then return 1 and the recursion statement as well. then the user input of the desired number and then the function is called to give the result.

Task 2 this task aims to ask the user for a number as input and use the math module to calculate the square root of the number, natural logarithm (log base e) of the number and sine of the number (in radians) and displays the calculated results.

Program of task 2 ass3task2.py

import math num=int(input("enter a number: ")) square_root=math.sqrt(num) print(f"square root of: {square_root}") natural_log=math.log(num) print(f"natural log: {natural_log}") sine=math.sin(num) print(f"sine: {sine}") input("press enter to exit")

Explanation of task 2 program here first math module is imported and from the math module functions for square root, logarithm and sine are used and thr result are then printed.

Status it has been verified before submission that the program runs successfully.
