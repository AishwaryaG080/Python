def main():
    fname = input("Enter file name: ")
    word = input("Enter word to search: ")

    f = open(fname, "r")
    data = f.read()
    f.close()

    if word in data:
        print("Word", word, "is found in", fname)
    else:
        print("Word", word, "is not found in", fname)

main()
