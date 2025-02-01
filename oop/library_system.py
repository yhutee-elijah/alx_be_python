class Book:
    """Represents a generic book with a title and an author."""

    def __init__(self, title, author):
        """Initializes the book's title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a user-friendly string representation of the Ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size} KB"

class EBook(Book):
    """Represents an electronic book with a file size."""

    def __init__(self, title, author, file_size):
        """Initializes the EBook with a file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a user-friendly string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size} KB"

class PrintBook(Book):
    """Represents a printed book with a page count."""
    
    def __init__(self, title, author, page_count):
        """Initializes the printBook with a page count."""
        super().__init__(title, author)
        self.page_count = page_count 

    def __str__(self):
        """Returns a user-friendly string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
class Library:
    """Represents a collection of books in a library."""    

    def __init__(self):
        """Initializes the library with an empty list of books."""
        self.books = []
        def add_book(self, book):
            """Adds a book (Book, Ebook, or PrintBook) to the library."""
            if isinstance(book, Book):
                self.books.append(book)
            else:
                raise TypeError("Only instances of Book, EBook, or PrintBook can be added.")
            

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)

        


