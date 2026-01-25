def main():
    n = int(input("Number of elements: "))
    numbers = list(map(int, input("Input elements: ").split()))
    x = int(input("Element to search: "))

    freq = 0
    for num in numbers:
        if num < x:
            freq += 1

    print("Output:", freq)

if __name__ == "__main__":
    main()
