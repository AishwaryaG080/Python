# Program 1 | length and width of a rectangle and print its area: 

def rect(length,width):
    area = length * width
    print("Area of rectangle:", area)

def main():
    length = int(input("Enter length of rectangle: "))
    width = int(input("Enter width of rectangle: "))
    rect(length,width)
    

if __name__ == "__main__":
    main()

# Program 2 | to accept the radius of a circle and print its area

def circle(r):
    area = 3.14159 * r * r 
    print("Area of circle:", area)

def main():
    r = int(input("Enter radius of circle: "))   
    circle(r) 

if __name__ == "__main__":
    main()

# Program 3 | Perfect Number

def perfect(num):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print(num, "is a Perfect Number")
    else:
        print(num, "is Not a Perfect Number")
def main():
    num = int(input("Enter a number: "))
    perfect(num)

if __name__ == "__main__":
    main()

# Program 4 | binary equivalent

def binary(num):
    if num > 1:
        binary(num // 2)  
    print(num % 2, end="")    

def main():
    num = int(input("Enter a number: "))
    print("Binary equivalent of", num, "is:", end=" ")
    if num == 0:
        print(0)
    else:
        binary(num)

if __name__ == "__main__":
    main()


# Program 5 | display grade

def grade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")
def main():
    marks = int(input("Enter the marks: "))
    grade(marks)

if __name__ == "__main__":
    main()

