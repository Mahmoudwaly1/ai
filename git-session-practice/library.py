class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: '{book.title}' to {self.name}.")

    def list_books(self):
        print(f"\n--- Books in {self.name} ---")
        for book in self.books:
            print(book)
        print("---------------------------\n")

    # ==========================================
    # NEW FEATURE TASK: Implement borrow_book
    # ==========================================
    def borrow_book(self, title):
         for book in self.books:
             if book.title == title:
                 if not book.is_borrowed:
                     book.is_borrowed = True
                     print(f"Success: '{book.title}' has been borrowed.")
                 else:
                     print(f"Error: '{book.title}' is already borrowed.")
                 return
         print(f"Error: '{title}' not found in the library.")
    # ==========================================

if __name__ == "__main__":
    my_library = Library("City Central Library")
    
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    
    my_library.add_book(book1)
    my_library.add_book(book2)
    
    my_library.list_books()
