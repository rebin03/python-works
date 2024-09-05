class Book:
    
    def __init__(self, title, author, price, language, genre):
        self.title = title
        self.author = author
        self.price = price
        self.language = language
        self.genre = genre
        
    def __str__(self):
        return self.title
        
    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}\nLanguage: {self.language}\nGenre: {self.genre}")
        
        
book1 = Book("Alchemist", "Paulo Coelho", 399, "English", "Noval")
book2 = Book("Atomic Habits", "James clear", 480, "English", "Self-help")

book1.display()
book2.display()

print(book1)
print(book2)