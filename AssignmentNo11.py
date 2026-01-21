#Program 1  | Prime Number

def main():
    num = int(input("Enter a number: "))
    
    if num <= 1:
        print("Not a Prime number")
        return
    
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime number")
            return
    
    print("Prime number")

if __name__ == "__main__":
    main()

#Program 2 | print count of digits

def main():
    num = int(input("Enter a number: "))
    count = 0
    
    if num == 0:
        count = 1
    else:
        while num > 0:
            num = num // 10
            count += 1

    print("Number of digits:", count)

if __name__ == "__main__":
    main()

#Program 3 | calculate the sum of digits

def main():
    num = input("Enter a number: ")
    sum_digits = 0
    
    for digit in num:
        if digit.isdigit():  
            sum_digits += int(digit)
    
    print("Sum of digits:", sum_digits)

if __name__ == "__main__":
    main()


#Program 4 | accept a number and print its reverse

def main():
    num = input("Enter a number: ")
    reversed_num = num[::-1]  
    print("Reversed number:", reversed_num)

if __name__ == "__main__":
    main()

#Program 5 | accept a number and print its reverse

def main():
    num = input("Enter a number: ")
    
    if num == num[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

if __name__ == "__main__":
    main()
