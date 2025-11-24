from catalog import Catalog
from book import Book

class LoanDesk:
    def __init__(self, catalog):
        self.catalog = catalog
        self.loans = {}  # key: ISBN, value: student or due-date

    def checkout(self, isbn, student):
        # lookup in catalog
        # update copies
        # add to loans
        pass

    def return_book(self, isbn):
        # remove from loans
        # update catalog copies
        pass

    def compute_fee(self, isbn, days_late):
        # polymorphic fee handling
        book = self.catalog.get_book(isbn)
        return book.calculate_fee(days_late)
