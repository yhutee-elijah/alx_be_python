class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
    def check_out(self):
        self.checked_out = True

    def return_book(self):
        self.checked_out = False

    def is_available(self):
        return not self.checked_out

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
    class Library:
        def __init__(self):
            self.books = []

        def add_book(self, book):
            self.books.append(book)

        def find_books(self, author):
            return [book for book in self.books if book.author == author]

        def find_available_books(self, author):
            return [book for book in self.books if book.author == author and book.is_available()]

        def __str__(self):
            return "\n".join([str(book) for book in self.books])
        
        if __name__ == "__main__":
            def main():