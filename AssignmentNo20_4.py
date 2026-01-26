import threading

def small(s):
    ch = 0
    for i in s:
        if i.islower():
            ch += 1
    print("Lowercase:", ch)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

def capital(s):
    ch = 0
    for i in s:
        if i.isupper():
            ch += 1
    print("Uppercase:", ch)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

def digits(s):
    ch = 0
    for i in s:
        if i.isdigit():
            ch += 1
    print("Digits:", ch)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

s = input("Enter string: ")

t1 = threading.Thread(target=small(s))
t2 = threading.Thread(target=capital(s))
t3 = threading.Thread(target=digits(s))

t1.start()
t2.start()
t3.start()
