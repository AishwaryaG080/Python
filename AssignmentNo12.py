#Program 1 | Vowel or Consonant

def main():
    char = input("Enter a character: ")
    if char in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")

if __name__ == "__main__":
    main()

#Program 2 | accept a number and print all its factors

def fact(num):

    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
        
def main():
    num = int(input("Enter a number: "))
    fact(num)
    
if __name__ == "__main__":
    main()

#Program 3 | Addition,Subtraction,Multiplication,Division

def Addition(Value1, Value2):
    Ans = 0     
    Ans = Value1 + Value2
    return Ans

def Subtraction(Value1, Value2):
    Ans = 0     
    Ans = Value1 - Value2
    return Ans

def Multiplication(Value1, Value2):
    Ans = 0     
    Ans = Value1 * Value2
    return Ans

def Division(Value1, Value2):
    Ans = 0     
    Ans = Value1 / Value2
    return Ans

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Result = Addition(No1,No2)
    print("Addition is : ",Result)

    Result = Subtraction(No1,No2)
    print("Subtraction is : ",Result)

    Result = Multiplication(No1,No2)
    print("Multiplication is : ",Result)

    Result = Division(No1,No2)
    print("Division is : ",Result)


if __name__ == "__main__":
    main()


#Program 4 | accept a number and print that many numbers starting from 1

def num(n):
    i = 1
    while i <= n:
        print(i)
        i += 1

def main():
    n = int(input("Enter a number: "))
    num(n)
    
if __name__ == "__main__":
    main()

#Program 5 | accept a number and print that many numbers in reverse order

def num(n):
    while n>0:
        print(n)
        n-= 1

def main():
    n = int(input("Enter a number: "))
    num(n)
    
if __name__ == "__main__":
    main()