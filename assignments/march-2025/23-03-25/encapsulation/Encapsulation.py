class Book:
    def __init__(self, title, author, isbn, available=False, borrower=None):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = available
        self.__borrower = borrower
    
    # Getters and setters for Book
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_available(self):
        return self.__available
    
    def set_available(self, available=False):
        self.__available = available

    def get_borrower(self):
        return self.__borrower

    def set_borrower(self, borrower=None):
        self.__borrower = borrower


class Library:
    def __init__(self, name, books=[], max_borrow_limit=0, members={}):
        self.__books = books
        self.__name = name
        self.__max_borrow_limit = max_borrow_limit
        self.__members = members

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

    def is_book_exist_by_isbn(self, isbn):
        book_existence_msg = "Book is not found"
        for book in self.__books:
            if book.get_isbn() == isbn:
                book_existence_msg = "Book is found"
        return book_existence_msg


# Example Usage
if __name__ == "__main__":
    # Create Library and Books
    library = Library("City Library")
    book1 = Book("Book1", "Author1", "1234567890")
    book2 = Book("Book2", "Author", "9876543210")

    # Read only properties
    childrenBook = Book("Three Little Pigs", "Author1", "1234567890")
    childrenBook.set_borrower('Shabab')
    
    library.add_book(book1)
    library.add_book(book2)
    
    # Borrow and Return Books
    print(library.borrow_book("1234567890"))
    print(library.return_book("1234567890"))
    
    # Remove a Book
    library.remove_book("9876543210")

    library.find_book_by_isbn("1234567890")
    print(library.is_book_exist_by_isbn("1234567890"))