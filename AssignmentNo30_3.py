def main():
    fname = input("Enter file name: ")

    f = open(fname, "r")

    for line in f:
        print(line, end="")

    f.close()

main()
