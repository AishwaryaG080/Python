def main():
    n = int(input("Input number of elements: "))
    total = sum(map(int, input("Input elements: ").split()))
    print("Output:", total)

if __name__ == "__main__":
    main()


