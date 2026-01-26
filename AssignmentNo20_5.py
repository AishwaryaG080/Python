import threading

def t1():
    for i in range(1, 51):
        print(i, end=" ")
    print()

def t2():
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()

th1 = threading.Thread(target=t1, name="Thread1")
th2 = threading.Thread(target=t2, name="Thread2")

th1.start()
th1.join()  

th2.start()
