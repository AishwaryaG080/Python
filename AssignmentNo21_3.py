import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for i in range(5):          
        lock.acquire()         
        counter += 1
        lock.release()          

def main():
    threads = []

    for i in range(3):          
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Final counter value:", counter)

main()
