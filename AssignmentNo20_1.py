import threading

def even():
    print("First 10 even numbers:")
    for i in range(2, 10, 2):
        print(i, end=" ")
    print()

def odd():
    print("First 10 odd numbers:")
    for i in range(1, 10, 2):
        print(i, end=" ")
    print()

t1 = threading.Thread(target=even)
t2 = threading.Thread(target=odd)

t1.start()
t2.start()

t1.join()
t2.join()
