class Library:
  
    def __init__(self):
        # List to store all books
        self._inventory = []
        # List to store all loan records
        self._records = []

    def add_book(self, book: LibraryItem):
        # Add a book to the inventory
        if not isinstance(book, LibraryItem):
            raise ValueError("Can only add LibraryItem objects")
        self._inventory.append(book)

    def remove_book(self, isbn: str) -> bool:
        # Remove a book by ISBN
        for book in self._inventory:
            if book.isbn == isbn:
                self._inventory.remove(book)
                return True
        return False

    def search_books(self, keyword: str) -> list:
        # Search for books by title or author (case-insensitive)
        keyword = keyword.lower()
        return [
            book for book in self._inventory
            if keyword in book.title.lower() or keyword in book.author.lower()
        ]
