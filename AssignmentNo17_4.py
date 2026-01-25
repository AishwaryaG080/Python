def fact(n):
    sum = 0

    for i in range(1, n + 1):
        if n % i == 0:
            sum = sum + i

    print("Sum of factors:", sum)

def main():
    n = int(input("Enter a number: "))
    fact(n)

if __name__ == "__main__":
    main()
