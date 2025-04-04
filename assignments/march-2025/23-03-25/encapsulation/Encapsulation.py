class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = True
        self.__borrower = None
    
    # Getter methods for Book attributes (read-only after creation)
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    # Getter and Setter for availability
    def get_available(self):
        return self.__available
    
    def set_available(self, available):
        self.__available = available
    
    # Getter and Setter for borrower
    def get_borrower(self):
        return self.__borrower
    
    def set_borrower(self, borrower_name):
        if borrower_name and self.__available:
            self.__borrower = borrower_name
            self.__available = False
        elif not borrower_name:
            self.__borrower = None
            self.__available = True
        else:
            raise ValueError("The book is currently unavailable for borrowing.")


class Library:
    def __init__(self, name, max_borrow_limit):
        self.__name = name
        self.set_max_borrow_limit(max_borrow_limit)
        self.__books = []
        self.__members = {}
    
    # Getter for Library name (read-only)
    def get_name(self):
        return self.__name
    
    # Getter and Setter for max_borrow_limit
    def get_max_borrow_limit(self):
        return self.__max_borrow_limit
    
    def set_max_borrow_limit(self, value):
        if value < 1:
            raise ValueError("Max borrow limit cannot be less than 1.")
        self.__max_borrow_limit = value
    
    # Method to add a book
    def add_book(self, book):
        self.__books.append(book)
        print(f"Book '{book.get_title()}' by {book.get_author()} added to the library.")
    
    # Method to remove a book by ISBN
    def remove_book(self, isbn):
        for book in self.__books:
            if book.get_isbn() == isbn:
                self.__books.remove(book)
                print(f"Book with ISBN {isbn} has been removed from the library.")
                return
        print(f"Book with ISBN {isbn} not found in the library.")
    
    # Method to get a book by ISBN
    def get_book_by_isbn(self, isbn):
        for book in self.__books:
            if book.get_isbn() == isbn:
                return book
        print(f"Book with ISBN {isbn} not found.")
        return None
    
    # Method to borrow a book
    def borrow_book(self, member_name, isbn):
        if member_name not in self.__members:
            print(f"Member '{member_name}' is not registered.")
            return
        
        if len(self.__members[member_name]) >= self.get_max_borrow_limit():
            print(f"Member '{member_name}' has reached the borrow limit.")
            return
        
        book = self.get_book_by_isbn(isbn)
        if book and book.get_available():
            book.set_borrower(member_name)
            self.__members[member_name].append(book)
            print(f"Book '{book.get_title()}' borrowed by {member_name}.")
            return f"Book '{book.get_title()}' borrowed by {member_name}."
        print("Book not available.")
    
    # Method to return a book
    def return_book(self, member_name, isbn):
        if member_name not in self.__members:
            print(f"Member '{member_name}' is not registered.")
            return
        
        for book in self.__members[member_name]:
            if book.get_isbn() == isbn:
                book.set_borrower(None)
                book.set_available(True)
                self.__members[member_name].remove(book)
                print(f"Book '{book.get_title()}' returned by {member_name}.")
                return
        print(f"Book with ISBN {isbn} was not borrowed by {member_name}.")
    
    # Method to register a new member
    def register_member(self, member_name):
        if member_name in self.__members:
            print(f"Member '{member_name}' is already registered.")
        else:
            self.__members[member_name] = []
            print(f"Member '{member_name}' successfully registered.")


# Example usage
if __name__ == "__main__":
    library = Library("Shabab's Library", 3)
    
    # Create books
    book1 = Book("Random Book", "Shabab", "1234567890")
    book2 = Book("Random Book 2", "Aariz", "0987654321")
    book3 = Book("Random Book 3", "Azad", "1122334455")
    
    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Register members
    library.register_member("Shabab")
    library.register_member("Aariz")
    
    # Borrow books
    library.borrow_book("Shabab", "1234567890")
    library.borrow_book("Aariz", "0987654321")
    
    # Return books
    library.return_book("Aariz", "1234567890")
    
    # Remove book from the library
    library.remove_book("1122334455")
    
    # Get a book by ISBN and print its details
    book = library.get_book_by_isbn("1234567890")
    if book:
        print(f"Found book: {book.get_title()} by {book.get_author()}")