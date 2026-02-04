def main():
    f1 = input("Enter first file name: ")
    f2 = input("Enter second file name: ")

    file1 = open(f1, "r").read()
    file2 = open(f2, "r").read()

    if file1 == file2:
        print("Both files have same contents")
    else:
        print("Files contents are different")

main()
