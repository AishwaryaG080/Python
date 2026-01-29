class BookStore:
    noofbooks=0

    def __init__(self,name,author):
        self.name = input("Enter Book Name: ")
        self.author = input("Enter Author Name: ")
        
        BookStore.noofbooks +=1
    
    def display(self):
        print(f"{self.name} by {self.author}. No of books: {BookStore.noofbooks}")

Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.display()
    

        