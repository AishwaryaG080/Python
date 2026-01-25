def add(a,b):
    sum = a + b
    print("Addition is :",sum)

def sub(a,b):
    sum = a - b 
    print("Substraction is :",sum)

def mul(a,b):
    sum = a * b 
    print("Multiplication is :",sum)

def div(a,b):
    sum = a / b 
    print("Division is :",sum)

def main():
    a = int(input("Enter the number one: "))
    b = int(input("Enter the number two: "))   
    add(a,b)
    sub(a,b)
    mul(a,b)
    div(a,b)

if __name__ == "__main__":
    main()