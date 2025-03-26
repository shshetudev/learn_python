class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = True
    
    # Getters and setters for Book
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author
    
    def set_author(self, author):
        self.__author = author
    
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def get_available(self):
        return self.__available
    
    def set_available(self, available):
        self.__available = available


class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = []
    
    # Getters and setters for Library
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def add_book(self, book):
        self.__books.append(book)
    
    def remove_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book:
            self.__books.remove(book)
    
    def borrow_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book and book.get_available():
            book.set_available(False)
            return f"Book '{book.get_title()}' borrowed."
        return "Book not available."
    
    def return_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book:
            book.set_available(True)
            return f"Book '{book.get_title()}' returned."
        return "Book not found."
    
    def find_book_by_isbn(self, isbn):
        for book in self.__books:
            if book.get_isbn() == isbn:
                return book
        return None


# Example Usage
if __name__ == "__main__":
    # Create Library and Books
    library = Library("City Library")
    book1 = Book("Book1", "Author1", "1234567890")
    book2 = Book("Book2", "Author", "9876543210")
    
    library.add_book(book1)
    library.add_book(book2)
    
    # Borrow and Return Books
    print(library.borrow_book("1234567890"))
    print(library.return_book("1234567890"))
    
    # Remove a Book
    library.remove_book("9876543210")