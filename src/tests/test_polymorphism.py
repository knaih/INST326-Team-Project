#TEST FOR POLYMORPHISM
import unittest
from library_item import LibraryItem, Book, AudioBook

class TestPolymorphism(unittest.TestCase):

    def test_str_polymorphism(self):
        """__str__ should behave differently depending on subclass."""
        book = Book("1984", "Orwell", "111", "Dystopian")
        audio = AudioBook("Dune", "Herbert", "222", "Narrator X", 720)

        self.assertIn("Book —", str(book))
        self.assertIn("Audiobook —", str(audio))
      

    def test_polymorphism_in_collection(self):
        """A list of LibraryItem objects should call subclass versions of methods."""
        items = [
            Book("B1", "A1", "101", "Fantasy"),
            AudioBook("A1", "A2", "202", "Narrator Y", 300),
        ]

        results = [str(item) for item in items]

        self.assertTrue(results[0].startswith("Book —"))
        self.assertTrue(results[1].startswith("Audiobook —"))

    def test_polymorphic_checkout(self):
        """Subclasses inherit checkout and behave uniformly."""
        b = Book("Book", "Author A", "333", "Sci-Fi")
        a = AudioBook("Audio", "Author B", "444", "Narrator Z", 120)

        for item in (b, a):  # treating them uniformly through base class
            item.checkout()
            self.assertFalse(item.available)


