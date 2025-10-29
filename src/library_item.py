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

    def check_availability(self):
        return self._available

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
        return f"LibraryItem(title={self._title!r}, author={self._author!r}, isbn={self._isbn!r}, available={self._available!r})"
