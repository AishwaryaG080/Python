from functools import reduce

def checkeven(no):
    return no % 2 == 0

def square(no):
    return no ** 2

def add(a, b):
    return a + b

def main():
   
    data = list(map(int, input("Enter numbers: ").split()))

    fdata = list(filter(checkeven, data))
    print("Data after filter:", fdata)

    mdata = list(map(square, fdata))
    print("Data after map:", mdata)

    rdata = reduce(add, mdata) if mdata else 0
    print("Data after reduce:", rdata)

if __name__ == "__main__":
    main()
