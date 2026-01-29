class circle ():
    def __init__(self):
        self.radius=0
        self.area=0
        self.circumference=0
        self.pi=3.14

    def accept(self):
        self.radius=int(input("Enter the radius of the circle: "))

    def calculatearea(self):
        self.area=self.pi*self.radius*self.radius

    def calculatecircumference(self):
        self.circumference= 2*self.pi*self.radius

    def display(self):
        print("Radius: ", self.radius)
        print("Area: ",self.area)
        print("Circumference: ",self.circumference)

obj=circle()
obj.accept()
obj.calculatearea()
obj.calculatecircumference()
obj.display()



      