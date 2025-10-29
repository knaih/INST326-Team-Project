class LibraryItem:

    def __init__(self, title: str, author: str, isbn: str, available: bool = True):
        self._title = title          # Book title
        self._author = author        # Book author
        self._isbn = isbn            # Book ISBN number
        self._available = available  # Availability status

    @property
    def title(self) -> str:
        """Return the book title."""
        return self._title

    @property
    def author(self) -> str:
        """Return the book author."""
        return self._author

    @property
    def isbn(self) -> str:
        """Return the book ISBN."""
        return self._isbn

    @property
    def available(self) -> bool:
        """Return whether the book is available."""
        return self._available

    def check_availability(self) -> bool:
        """Check if the book is available."""
        return self._available

    def update_info(self, title: str = None, author: str = None, isbn: str = None):
        """Update the book information."""
        if title:
            self._title = title
        if author:
            self._author = author
        if isbn:
            self._isbn = isbn

    def __str__(self) -> str:
        """Return a human-readable string for the book."""
        status = "Available" if self._available else "Checked out"
        return f"{self._title} by {self._author} ({status})"

    def __repr__(self) -> str:
        """Return a detailed representation for debugging."""
        return f"LibraryItem(title={self._title!r}, author={self._author!r}, isbn={self._isbn!r}, available={self._available!r})"

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
