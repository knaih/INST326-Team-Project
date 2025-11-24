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
        
from item import LibraryItem   # or whatever your team calls it
### Deliverables ###
class Catalog:
    def __init__(self):
        self.items = []     # composition → Catalog HAS-A list of items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        self.items = [i for i in self.items if i.id != item_id]

    def search(self, title):
        return [i for i in self.items if title.lower() in i.title.lower()]
