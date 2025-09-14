class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def showInfo(self):
        print(f"The Library has {self.noBooks} books and The Books are:")
        for book in self.books:
            print(book)
l1=Library()
l1.addBook("Harry Potter")
l1.addBook("Muna Madan")
l1.addBook("Ramayan")
l1.showInfo() 