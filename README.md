## Assignment-4
this repository contains two task each for the assignment 4 of tutedude python program

## Task 1
this task aims to open and read a text file named sample.txt and print its content line by line. it should also handle errors gracefully if the file does not exist.

## Program of task 1

[ass4task1.py](https://github.com/user-attachments/files/24332672/ass4task1.py)

import os
file="sample.txt"
if os.path.exists(file):
    print(f"file {file} exists")
    print("======================")
    fh=open(file,"r")
    line1= fh.readline()
    line2= fh.readline()
    fh.close()
    print(f'line1: {line1}')
    print(f'line2: {line2}')
    print("======================")
else:
    print(f"file {file} does not exist")
    print("======================")
input("press enter to exit")
print("======================")


## Explanation of task 1 program
here first os module is imported and then with the help of os.path.exists function , it is checked if the file exists or not and if the file exists then readline function is used to print line. if the file does not exist then with else statement the messase stating the same is printed.

## Task 2 
this task aims to take user input and writes it to a file named output.txt. and append additional data to the same file. it should also read and display the final content of the file.

## Program of task 2

[ass4task2.py](https://github.com/user-attachments/files/24332739/ass4task2.py)

content=input("enter text to write to the file: ")
fh=open("output.txt","xt")
fh.write(content)
fh.write("\n")
fh.close()
print("data successfully written to output.txt")
print("========================")

addition=input(" enter additional text to append: ")
fh=open("output.txt","at")
fh.write(addition)
fh.close()
print("data successfully appended to output.txt")
print("========================")

fh=open("output.txt","rt")
text=fh.read()
fh.close()

print("final content of output.txt")
print(text)

print("========================")
input("press enter to exit")


## Explanation of task 2 program 
here the user input is written in the output.txt file with write function then the same file is appended in append mode and then the file is read and the final content is printed in the end.

## Status 
it has been verified before submission that the program runs successfully.
