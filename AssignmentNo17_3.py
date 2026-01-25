def fact(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        print("Factorial is:", fact)

def main():
    n = int(input("Enter a number: "))
    fact(n)

if __name__ == "__main__":
    main()
