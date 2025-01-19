class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.is_available = True 

      def check_out(self):
        if self.is_available:
            self.is_available = False
            return True  # Successfully checked out
        else:
            return False  # Book already checked out

    def return_book(self):
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                if book.check_out():
                    print(f"{title} checked out successfully.")
                    return
        print(f"'{title}' not found or already checked out.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"'{title}' returned successfully.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book.title for book in self.books if book.is_available]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books currently available.")

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()
        
