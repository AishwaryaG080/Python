def main():
    n = int(input("Enter the number: "))   
    n = 1

    for i in range(1, 5):
        for j in range(i):
            print(n, end=" ")
            n += 1
            if n > 5:
                n = 1
        print()
if __name__ == "__main__":
    main()