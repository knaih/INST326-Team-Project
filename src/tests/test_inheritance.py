#testing inheritance
import unittest
from library_item import LibraryItem, Book, AudioBook

class TestInheritance(unittest.TestCase):

    def test_book_is_subclass_of_libraryitem(self):
        """Book should inherit from LibraryItem."""
        self.assertTrue(issubclass(Book, LibraryItem))

    def test_audiobook_is_subclass_of_libraryitem(self):
        """AudioBook should inherit from LibraryItem."""
        self.assertTrue(issubclass(AudioBook, LibraryItem))

    def test_book_instance_is_libraryitem_instance(self):
        """Book instances should be instances of LibraryItem."""
        b = Book("Test", "Author", "123", "Fiction")
        self.assertIsInstance(b, LibraryItem)

    def test_audiobook_instance_is_libraryitem_instance(self):
        """AudioBook instances should be instances of LibraryItem."""
        a = AudioBook("Test", "Author", "123", "Narrator", 60)
        self.assertIsInstance(a, LibraryItem)

    def test_libraryitem_is_not_abstract(self):
        """
        Since the provided class wrongly isn't abstract,
        this test confirms it can be instantiated (even though it shouldn't).
        """
        item = LibraryItem("Title", "Author", "123")
        self.assertIsInstance(item, LibraryItem)

    def test_subclasses_inherit_methods(self):
        """Subclasses should inherit methods from LibraryItem."""
        b = Book("Test", "Author", "123", "Fiction")
        a = AudioBook("Test", "Author", "123", "Narrator", 60)

        # inherited attributes
        self.assertEqual(b.title, "Test")
        self.assertEqual(a.title, "Test")

        # inherited methods
        b.checkout()
        self.assertFalse(b.available)

        a.checkout()
        self.assertFalse(a.available)

    def test_subclasses_override_str(self):
        """Check that __str__ is overridden."""
        b = Book("Test", "Author", "123", "Sci-Fi")
        a = AudioBook("Test", "Author", "123", "NarratorX", 120)

        # parent __str__()
        parent_str = LibraryItem("X", "Y", "Z").__str__()

        # child __str__ should differ
        self.assertNotEqual(parent_str, str(b))
        self.assertNotEqual(parent_str, str(a))


