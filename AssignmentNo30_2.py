def main():
    fname = input("Enter File name: ")

    f = open(fname, "r")
    data = f.read()
    f.close()

    words = data.split()
    count = len(words)
    
    print("Count of", fname, "is:", count)

main()
