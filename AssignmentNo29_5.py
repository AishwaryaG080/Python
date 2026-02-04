def main():
    fname = input("Enter File name: ")
    strnm = input("Enter String name: ")

    f = open(fname, "r")
    data = f.read()
    f.close()

    count= data.count(strnm)
    
    print("Count of", strnm, "is:", count)

main()
