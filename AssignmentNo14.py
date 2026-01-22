#Program No. 1 | square of no.

def square(n):
    check = lambda n: n*n
    print("square is :",check(n))

def main():
    n = int(input("Enter the number: "))
    square(n)

if __name__ == "__main__":
    main()
    
#Program No. 2 | cube of no.

def cube(n):
    check = lambda n: n*n*n
    print("Cube is :",check(n))

def main():
    n = int(input("Enter the number: "))
    cube(n)

if __name__ == "__main__":
    main()

#Program No. 3 | maximum no.

def max(a, b):
    sum = lambda a, b: a if a > b else b
    return sum(a, b)

def main():
    a = int(input("Enter first no.: "))
    b = int(input("Enter second no.: "))
    print("Maximum number is:", max(a, b))

if __name__ == "__main__":
    main()
    
#Program No. 4 | minimun no.

def min(a, b):
    sum = lambda a, b: a if a < b else b
    return sum(a, b)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Minimum number is:", min(a, b))

if __name__ == "__main__":
    main()

#Program No. 5 | Even or Odd
def main():
    Value = 0
    Ret = False

    CheckEven = lambda No : (No % 2 == 0)

    print("Enter number : ")
    Value = int(input())

    Ret = CheckEven(Value)

    if(Ret == True):
        print("It is Even")
    else:
        print("It is Odd")
    
if __name__ == "__main__":
    main()

#Program No. 6 | Odd or Even

def main():
    Value = 0
    Ret = False

    Checkodd = lambda No : (No % 2 != 0)

    print("Enter number : ")
    Value = int(input())

    Ret = Checkodd (Value)

    if(Ret == True):
        print("It is odd")
    else:
        print("It is even")
    
if __name__ == "__main__":
    main()


#Program No. 7 |check whether a number is divisible by 5
def div(n):
    check = lambda n: (n % 5 == 0)
    print("No. is divisible by 5:",check(n))

def main():
    n = int(input("Enter the number: "))
    div(n)

if __name__ == "__main__":
    main()

#Program No. 8 |Addition

def add(a,b):
    sum = lambda a,b: (a + b )
    print("Addition is :",sum(a,b))

def main():
    a = int(input("Enter the number one: "))
    b = int(input("Enter the number two: "))   
    add(a,b)

if __name__ == "__main__":
    main()

#Program No. 9 |Multiplication

def add(a,b):
    sum = lambda a,b: (a * b )
    print("Multiplication is :", sum(a,b))

def main():
    a = int(input("Enter the number one: "))
    b = int(input("Enter the number two: "))   
    add(a,b)

if __name__ == "__main__":
    main()

#Program No. 10 |Accept 3 nos and return largest

def check(a,b,c):
    largest = lambda a,b,c: a if(a>=b and a>=c) else (b if b>=c else c)
    print("Largest no. is : ",largest(a,b,c))

def main():
    a = int(input("Enter the number one: "))
    b = int(input("Enter the number two: "))   
    c = int(input("Enter the number three: ")) 
    check(a,b,c)

if __name__ == "__main__":
    main()