"""
Library Management System - Demo Script

This script demonstrates the key functions in our library management system with realistic library scenarios.

Author: Anyi Tasong ( Group Member )
"""

from datetime import date
from src.persistence import load_data, save_data, export_books
from src.library_functions import (
    total_books,
    book_titles,
    add_books,
    remove_books,
    update_book_info,
    books_checked_out,
    check_membership,
    fine_amount,
    calculate_due_date,
    search_books,
    validate_isbn,
    overdue_books,
    send_overdue_notification,
)


def load_or_initialize():
    """Load library data or initialize empty structures if file is missing."""
    data = load_data("data/library_data.json")
    inventory = data.get("books", [])
    members = data.get("members", {
        "M100": {"name": "Alice", "active": True},
        "M101": {"name": "Bob", "active": True},
    })
    transactions = data.get("events", [])
    return inventory, members, transactions, data


def scenario_populate_inventory(inventory):
    """Staff adds initial books to the inventory."""
    print("\n--- Scenario: Library opening & inventory population ---")
    books_to_add = [
        {"isbn": "9780306406157", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"isbn": "9780143127741", "title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"isbn": "9780061120084", "title": "1984", "author": "George Orwell"},
    ]
    add_books(inventory, books_to_add)
    print("Added books. Total unique titles now:", total_books(inventory))
    print("Titles:", book_titles(inventory))


def scenario_member_borrows(inventory, members, transactions):
    """Member M100 borrows '1984'."""
    print("\n--- Scenario: Member borrows a book ---")
    hits = search_books(inventory, "1984")
    if not hits:
        print("Book '1984' not found in inventory.")
        return
    isbn = hits[0]["isbn"]
    member_id = "M100"

    status = check_membership(members, member_id)
    print(f"Member {member_id} status:", status)
    if status != "Active" or not validate_isbn(isbn):
        return

    checkout_date = date(2025, 10, 1)
    transactions.append({"isbn": isbn, "member_id": member_id, "action": "checkout", "date": checkout_date.isoformat()})
    print(f"Member {member_id} checked out ISBN {isbn} on {checkout_date}")
    print("Due date:", calculate_due_date(checkout_date, 14))


def scenario_return_and_overdue(transactions):
    """Process a late return and detect overdue items."""
    print("\n--- Scenario: Return processing & overdue detection ---")
    return_date = date(2025, 10, 20)
    for tx in transactions:
        if tx["action"] == "checkout":
            transactions.append({"isbn": tx["isbn"], "member_id": tx["member_id"], "action": "return", "date": return_date.isoformat()})
            print(f"Processed return for member {tx['member_id']} on {return_date} (ISBN {tx['isbn']})")
            break

    overdue_list = overdue_books(transactions, return_date.isoformat())
    for item in overdue_list:
        member = item.get("member_id", "UNKNOWN")
        title = item.get("title", item.get("isbn", "Unknown"))
        print(f"Sending overdue notification to {member} for {title}")
        send_overdue_notification(member, title)


def scenario_staff_tasks(inventory):
    """Staff operations: search, remove, report."""
    print("\n--- Scenario: Staff tasks & reporting ---")
    print("Searching for 'Orwell':", search_books(inventory, "Orwell"))
    remove_isbn = "9780143127741"
    removed = remove_books(inventory, remove_isbn)
    print(f"Attempted to remove ISBN {remove_isbn}: Removed = {removed}")
    print("Inventory titles now:", book_titles(inventory))


def scenario_fines_and_updates():
    """Compute fines for overdue transactions."""
    print("\n--- Scenario: Compute fines & update records ---")
    days_overdue = 5
    print(f"Computed fine for {days_overdue} days overdue: ${fine_amount(days_overdue):.2f}")


def run_demo():
    print("=== Scenario-Based Library Demo ===")
    inventory, members, transactions, data = load_or_initialize()

    scenario_populate_inventory(inventory)
    scenario_member_borrows(inventory, members, transactions)
    scenario_staff_tasks(inventory)
    scenario_return_and_overdue(transactions)
    scenario_fines_and_updates()

    print("\n--- Final Summary ---")
    print("Total unique books:", total_books(inventory))
    print("Titles remaining:", book_titles(inventory))
    print("Total currently checked out:", books_checked_out(transactions))

    # Save and export
    data["books"] = inventory
    data["members"] = members
    data["events"] = transactions
    save_data(data, "data/library_data.json")
    export_books(inventory, "data/books_report.txt")

    print("\n=== End Scenario ===")


if __name__ == "__main__":
    run_demo()
