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

    def total_books(self) -> int:
        # Return total number of books
        return len(self._inventory)

    def all_titles(self) -> list:
        # Return list of all book titles
        return [book.title for book in self._inventory]

    def get_overdue_books(self, current_day: datetime) -> list:
        # Return a list of overdue books
        overdue = []
        for loan in self._records:
            if loan.is_overdue(current_day):
                overdue.append(loan.book)
        return overdue

    def issue_book(self, isbn: str, member: Member, issue_date: datetime, due_date: datetime) -> str:
        # Issue a book to a member
        if not member.is_active():
            return f"Member {member.name} is inactive."

        # Find the book in inventory
        for book in self._inventory:
            if book.isbn == isbn:
                if not book.available:
                    return f"The book '{book.title}' is currently not available."

                # Mark the book as unavailable
                book._available = False

                # Create a new loan record
                loan = Loan(member, book, issue_date, due_date)
                self._records.append(loan)

                return f"Book '{book.title}' has been issued to {member.name}."

        return "Book not found in inventory."

    def __str__(self):
        # Return a simple summary of the library
        return f"Library with {len(self._inventory)} books and {len(self._records)} active loans."

    def __repr__(self):
        # Return detailed representation for debugging
        return f"Library(inventory={self._inventory!r}, records={self._records!r})"
