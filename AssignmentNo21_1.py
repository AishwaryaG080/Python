import threading

def prime(n):
    print("Prime:")
    for x in n:
        if x > 1 and all(x % i != 0 for i in range(2, x)):
            print(x, end=" ")
    print()

def nonprime(n):
    print("Non-Prime:")
    for x in n:
        if x <= 1 or any(x % i == 0 for i in range(2, x)):
            print(x, end=" ")
    print()

n = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=prime(n))
t2 = threading.Thread(target=nonprime(n))

t1.start()
t2.start()
