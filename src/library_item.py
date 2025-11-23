class LibraryItem:

    def __init__(self, title: str, author: str, isbn: str, available: bool = True):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = available

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def available(self):
        return self._available

    def check_availability(self) -> bool:
        return self._available

    def checkout(self) -> None:
        if not self._available:
            raise ValueError(f"'{self._title}' is already checked out.")
        self._available = False

    def return_item(self) -> None:
        self._available = True

    def update_info(self, title=None, author=None, isbn=None):
        if title:
            self._title = title
        if author:
            self._author = author
        if isbn:
            self._isbn = isbn

    def __str__(self):
        status = "Available" if self._available else "Checked out"
        return f"{self._title} by {self._author} ({status})"

    def __repr__(self):
        return (
            f"LibraryItem(title={self._title!r}, author={self._author!r}, "
            f"isbn={self._isbn!r}, available={self._available!r})"
        )


class Book(LibraryItem):

    def __init__(self, title: str, author: str, isbn: str, genre: str, available: bool = True):
        super().__init__(title, author, isbn, available)
        self.genre = genre

    def __str__(self):
        base = super().__str__()
        return f"Book — {base}, Genre: {self.genre}"


class AudioBook(LibraryItem):

    def __init__(self, title: str, author: str, isbn: str, narrator: str, duration_minutes: int, available: bool = True):
        super().__init__(title, author, isbn, available)
        self.narrator = narrator
        self.duration_minutes = duration_minutes

    def __str__(self):
        base = super().__str__()
        return f"Audiobook — {base}, Narrator: {self.narrator}, Duration: {self.duration_minutes} mins"
