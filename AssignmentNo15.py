# Program No 1| Square of each number using map 
def square(n):
    return n * n

def main():
    lst = list(map(int, input("Enter numbers: ").split()))
    squared = list(map(square, lst))
    print("Squared list:", squared)
  
if __name__ == "__main__":
    main()

# Program No 2| Even number using filter 

def is_even(n):
    return n % 2 == 0

def main():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    even_numbers = list(filter(is_even, lst))
    print("Even numbers:", even_numbers)

if __name__ == "__main__":
    main()

# Program No 3| Odd number using filter 

def is_odd(n):
    return n % 2 != 0

def main():
    odd = list(map(int, input("Enter numbers : ").split()))
    even_numbers = list(filter(is_odd, odd))
    print("Odd numbers:", even_numbers)

if __name__ == "__main__":
    main()

# Program No 4| lambda with reduce() to add all numbers

from functools import reduce

def main():
    display = list(map(int, input("Enter numbers : ").split()))
    total = reduce(lambda a, b: a + b, display)
    print("Sum of numbers:", total)

if __name__ == "__main__":
    main()

#Program No. 5 | maximun no.

from functools import reduce

def maximum(a, b):
    return reduce(lambda x, y: x if x > y else y, [a, b])

def main():
    a = int(input("Enter first no.: "))
    b = int(input("Enter second no.: "))
    print("Maximum number is:", maximum(a, b))

if __name__ == "__main__":
    main()

#Program No. 6 | minimum no.

from functools import reduce

def minimum(a, b):
    return reduce(lambda x, y: x if x < y else y, [a, b])

def main():
    a = int(input("Enter first no.: "))
    b = int(input("Enter second no.: "))
    print("Minimum number is:", minimum(a, b))

if __name__ == "__main__":
    main()

# Program No 7 | Filter strings with length > 5

def main():
    display = input("Enter strings: ").split()
    result = list(filter(lambda s: len(s) > 5, display))
    print("Strings with length > 5:", result)

if __name__ == "__main__":
    main()

# Program No 8 | Nos divisible by 3 and 5 using filter

def main():
    display = list(map(int, input("Enter numbers: ").split()))
    result = list(filter(lambda a: a % 3 == 0 and a % 5 == 0, display))
    print("Nos divisible by 3 and 5:", result)

if __name__ == "__main__":
    main()

# Program No 9 | Product of all elements

from functools import reduce

def main():
    display = list(map(int, input("Enter numbers: ").split()))
    result = reduce(lambda a, b: a * b, display)
    print("Product of all numbers:", result)

if __name__ == "__main__":
    main()

# Program No 10 | count of even nos

from functools import reduce

def main():
    display = input("Enter numbers: ").split()
    counte = reduce(lambda count, a: count + (int(a) % 2 == 0), display, 0)
    print("Count of even numbers:", counte)

if __name__ == "__main__":
    main()









