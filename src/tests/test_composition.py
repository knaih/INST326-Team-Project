#testing member from import loan
#member class
import unittest
from member import Member
from loan import Loan
from library_item import Book

class TestComposition(unittest.TestCase):

    def test_member_has_loans(self):
        member = Member("Alice", "M001")
        book = Book("Dune", "Frank Herbert", "ISBN123", "Sci-Fi")

        loan = Loan(member, book)
        member.add_loan(loan)

        self.assertIn(loan, member.loans)

    def test_member_can_remove_loan(self):
        member = Member("Alice", "M001")
        book = Book("Dune", "Frank Herbert", "ISBN123", "Sci-Fi")

        loan = Loan(member, book)

        member.add_loan(loan)
        member.remove_loan(loan)

        self.assertNotIn(loan, member.loans)

    def test_loan_contains_member_and_item(self):
        member = Member("Alice", "M001")
        book = Book("Dune", "Frank Herbert", "ISBN123", "Sci-Fi")
        loan = Loan(member, book)

        self.assertEqual(loan.member, member)
        self.assertEqual(loan.item, book)

