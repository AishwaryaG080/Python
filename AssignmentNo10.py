#Program 1 | Multiplication table of the no

def multiply(no):
    for i in range(1, 11):
        print( no * i)

def main():
    no = int(input("Enter the no.: "))
    multiply(no)

if __name__ == "__main__":
    main()


#Program 2 | Sum of first N Natural no.

def natural(n):
    
    for i in range(1, n + 1):
        sum = 0
        sum += i
        print("natural numbers", sum)


def main():
    n = int(input("Enter a number: "))
    natural(n)

if __name__ == "__main__":
    main()


#Program 3 | Factorial

def factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i
    print("Factorial of", no, "is:", fact)

def main():
    no = int(input("Enter the no.: "))
    factorial(no)

if __name__ == "__main__":
    main()

#Program 4 | Even No.

def CheckEven(No):
    if No % 2 == 0:
        return True
    else:
        return False

def main():
    Value = int(input("Enter number: "))

    sum = CheckEven(Value)

    if sum == True:
        print("It is Even")
    else:
        print("It is Odd")

if __name__ == "__main__":
    main()


# Program 5 | Odd no.

def CheckOdd(No):
    if No % 2 != 0:
        return True
    else:
        return False

def main():
    Value = int(input("Enter number: "))

    sum = CheckOdd(Value)

    if sum == True:
        print("It is Odd")
    else:
        print("It is Even")

if __name__ == "__main__":
    main()