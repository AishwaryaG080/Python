from functools import reduce

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def double(num):
    return num * 2

def maximum(a, b):
    return a if a > b else b

def main():
    data = list(map(int, input("Enter numbers separated by space: ").split()))

    primes = list(filter(is_prime, data))
    print("Prime numbers are:", primes)

    doubled = list(map(double, primes))
    print("Doubled prime numbers are:", doubled)

    if doubled:
        max_val = reduce(maximum, doubled)
        print("Maximum among doubled primes is:", max_val)
    else:
        print("No prime numbers in the list.")

if __name__ == "__main__":
    main()
