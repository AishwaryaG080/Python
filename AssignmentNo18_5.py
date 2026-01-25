import MarvellousNum

def ListPrime():
 N = int(input("Enter number of elements: "))
 numbers = []

 for i in range(N):
        numbers.append(int(input(f"Enter element {i+1}: ")))

 sum_primes = 0
 for num in numbers:
    if MarvellousNum.ChkPrime(num):
        sum_primes += num

 return sum_primes

# Main program
print("Sum of prime numbers:", ListPrime())