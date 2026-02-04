fname = input("Enter File name: ")

f = open(fname, "r")
count = len(f.readlines())
f.close()
print("Count of lines in", fname, "is:", count)

