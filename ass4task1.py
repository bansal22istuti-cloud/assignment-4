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


