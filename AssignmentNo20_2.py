import threading

def EvenFactor(no):
    s = 0
    print("Even factors of", no, "are:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i, end=" ")
            s = s + i
    print("Sum of even factors:", s)

def OddFactor(no):
    s = 0
    print("Odd factors of", no, "are:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i, end=" ")
            s = s + i
    print("Sum of odd factors:", s)

def main():
    no = 10 

    t1 = threading.Thread(target=EvenFactor(no))
    t2 = threading.Thread(target=OddFactor(no))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

main()
