class Book:
    def __init__(self, title, author, year):
        """Inittializes the book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        """called when the Book instance is deleted."""
        print(f"Deleting {self.title}")
    def __str__(self):
        """Returns a readable string representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        """Returns an official string representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
