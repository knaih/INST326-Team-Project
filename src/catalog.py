class Catalog:
    @property
    def __init__(self):
        self._inventory[]
        
    @property   
    def __init__(self, name):
        self._name = name
        self._inventory = []

    @property
    def name(self):
        #name
        return self._name

    @property
    def inventory(self):
        return list(self._inventory)

    @property
    def total_books(self):
        return total_books(self._inventory)
        
        #instance methods
    def search(search, query):
        return search_books(self._inventory, query)

    def remove_book(self, isbn):
        remove_books(self._inventory, isbn)

    def add_book(self, isbn, title, author):
        isbn = isbn.strip()
        title = title.strip()
        author = author.strip()
        book_entry = {"isbn": isbn, "title": title, "author": author}
        add_books(self._inventory, book_entry)
        
