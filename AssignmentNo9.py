#Program 1 | Print Jay Ganesh
def Display():
    print("Jay Ganesh")

def main():
    Display()

if __name__ == "__main__":
    main()


#Program 2 | Print Jay Ganesh

def ChkGreater(no1,no2):
    if no1>no2:
        print("The greater no is:",no1)
    else:
        print("The greater no is:",no2)

def main():
    no1=input("Enter first no.:")    
    no2=input("Enter second no.:")

    ChkGreater(no1,no2)
    
    
if __name__ == "__main__":
    main()


#Program 3 | Print square of no.
def square(no):
    result=no*no
    print("The square is :",result)

def main():
    no=int(input("Enter the no."))
    square(no)

if __name__ == "__main__":  
    main()

#Program 4 | Print cube of no.
def cube(no):
    result=no**3
    print("The cube is:",result)

def main():
    no=int(input("Enter the no."))
    cube(no)

if __name__ == "__main__":
    main()

#Program 5 | To check no. divisible by 3 & 5
def div(no):
    if no % 3 == 0 and no % 5 == 0:
        print("No is divisible by 3 and 5")
    else:
        print("No is not divisible by 3 and 5")

def main():
    no=int(input("Enter the no."))
    div(no)

if __name__ == "__main__":
    main()
