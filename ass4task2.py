
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

