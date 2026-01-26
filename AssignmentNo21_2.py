import threading

def maximum(a, b):
    print("Maximum No:")
    if a > b:
        print(a)
    else:
        print(b)

def minimum(a, b):
    print("Minimum No:")
    if a < b:
        print(a)
    else:
        print(b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

t1 = threading.Thread(target=maximum(a, b))
t2 = threading.Thread(target=minimum(a, b))

t1.start()
t2.start()
