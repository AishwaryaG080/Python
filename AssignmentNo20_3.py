import threading

def EvenList(n):
    lst = 0
    print("Even elements:")
    for i in n:
        if i % 2 == 0:
            print(i, end=" ")
            lst = lst + i
    print("\nSum of even elements:", lst)

def OddList(n):
    lst = 0
    print("Odd elements:")
    for i in n:
        if i % 2 != 0:
            print(i, end=" ")
            lst = lst + i
    print("\nSum of odd elements:", lst)

def main():
    n = list(map(int, input("Enter integers: ").split()))

    t1 = threading.Thread(target=EvenList(n))
    t2 = threading.Thread(target=OddList(n))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

main()
