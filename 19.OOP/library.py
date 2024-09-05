class Book:
    
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        
    def __str__(self):
        return self.title
    
class Library:
    
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        for book in self.books:
            print(book)
    

book1 = Book("Aadujeevitham", "Benyamin", "Novel")
book2 = Book("The 5 am club", "Robin Sharma", "self-help")
book3 = Book("Atomic Habits", "James clear", "self-help")

library1 = Library("Public library", "Ernakulam")

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)

library1.list_books()