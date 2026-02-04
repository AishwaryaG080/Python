import sys
import os

f1 = open(sys.argv[1], "r")
data = f1.read()
f1.close()

f2 = open("Demo.txt", "w")
f2.write(data)
f2.close()

print("File copied to Demo.txt")
