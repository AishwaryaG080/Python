class arithmatic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def accept(self):
        self.value1=int(input("Enter 1st No.: ",))
        self.value2=int(input("Enter 2nd No.: ",))
    
    def addition(self):
        return self.value1+self.value2
    def multiplication(self):
        return self.value1*self.value2
    def substraction(self):
        return self.value1-self.value2

    def division(self):
        if self.value2 == 0:
            return "Error: Division by zero is not allowed"
        else:
            return self.value1 / self.value2
        
obj = arithmatic()
obj.accept()

print("Addition:", obj.addition())
print("Subtraction:", obj.substraction())
print("Multiplication:", obj.multiplication())
print("Division:", obj.division())
    
    

        