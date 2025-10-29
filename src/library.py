class Library:

    def __init__(self):
        self._inventory = []  # List of LibraryItem objects
        self._records = []    # List of Loan objects (to track issued books)

    def add_book(self, book: LibraryItem):
        if not isinstance(book, LibraryItem):
            raise ValueError("Can only add LibraryItem objects")
        self._inventory.append(book)

    def remove_book(self, isbn: str) -> bool:
        for book in self._inventory:
            if book.isbn == isbn:
                self._inventory.remove(book)
                return True
        return False

    def search_books(self, keyword: str) -> list:
        keyword = keyword.lower()
        return [book for book in self._inventory
                if keyword in book.title.lower() or keyword in book.author.lower()]

    def total_books(self) -> int:
        return len(self._inventory)

    def all_titles(self) -> list:
        return [book.title for book in self._inventory]
