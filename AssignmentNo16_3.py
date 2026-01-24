# Program No 1| write fun() & display hello
def fun():
    print("Hello from fun")

def main():
    fun()
if __name__ == "__main__":
     main()

# Program No 2| even odd

def chknum(no1,no2):
    if (no1 % 2 == 0) :
        print("Even number")
    else:
        print("Odd number")

def main():
    no1=int(input("Enter first no:"))
    no2=int(input("Enter second no"))
    chknum(no1,no2)

if __name__ == "__main__":
    main()

# Program No 3 | Addition
def add(no1,no2):
    sum=no1+no2
    print("Addition is :",sum)

def main(): 
    no1=int(input("Enter 1st no :"))
    no2=int(input("Enter 2nd no :"))
    add(no1,no2)

if __name__ == "__main__":
    main()

# Program No 4 | Display marvellous 5 times

def display():
    i=0
    while (i<5):
        print("Marvellous")
        i=i+1
    

def main():
    display()

if __name__ == "__main__":
    main()

# Program No 5 | Display 10 - 1 on screen

def display():

    for i in range (10,0,-1):
        print(i)

def main():
    display()

if __name__ == "__main__":
    main()

# Program No 6 | check if no is +ve or -ve

def display(no):

    if no>0:
        print("Positive")
    elif no<0:
        print("Negative")   
    else:
        print("Zero")  

def main():
    no=int(input("Enter no :"))
    display(no)

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

# Program No 8 | Display * on screen

def display(n):

    for i in range (n):
        print("*")
       
def main():
    n = int(input("Enter numbers: "))
    display(n)

if __name__ == "__main__":
    main()

# Program No 9 | Display first 10 even nos
def display(n):
    for i in range(2, 2*n + 1, 2):
        print(i)

def main():
    n = int(input("Enter how many even numbers to display: "))
    display(n)

if __name__ == "__main__":
    main()


# Program No 10  | Display length of input value

def main():
    value = input("Enter a value: ")
    print("Length of the value is:", len(value))

if __name__ == "__main__":
    main()
