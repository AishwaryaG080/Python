import threading

sum_result = 0
prod_result = 1

def compute_sum(lst):
    global sum_result
    sum_result = sum(lst)

def compute_product(lst):
    global prod_result
    prod = 1
    for x in lst:
        prod *= x
    prod_result = prod

lst = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=compute_sum, args=(lst,))
t2 = threading.Thread(target=compute_product, args=(lst,))


t1.start()
t2.start()

t1.join()
t2.join()

print("Sum:", sum_result)
print("Product:", prod_result)
