"""
Library Management System - Demo Script

This script demonstrates the key functions in our library management system with realistic library scenarios.

Author: Anyi Tasong ( Group Member )
"""

from datetime import date, timedelta

try:
    from src.library_functions import (
        total_books,
        book_titles,
        author_name,
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
        event_type,
        send_overdue_notification,
    )
except Exception as e:
    raise ImportError(
        "Could not import library functions. Ensure `src/library_functions.py` exists and "
        "exports the listed functions. Original error: {}".format(e)
    )


def setup_library():
    """Initial library setup: inventory, members, and an empty transactions ledger."""
    inventory = []
    members = {
        "M100": {"name": "Alice", "active": True},
        "M101": {"name": "Bob", "active": True},
    }
    transactions = []  # ledger of {"isbn","member_id","action","date"}
    return inventory, members, transactions


def scenario_populate_inventory(inventory):
    """Staff adds initial books to the inventory."""
    print("\n--- Scenario: Library opening & inventory population ---")
    books_to_add = [
        {"isbn": "9780306406157", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"isbn": "9780143127741", "title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"isbn": "9780061120084", "title": "1984", "author": "George Orwell"},
    ]
    try:
        add_books(inventory, books_to_add)
        print("Added books. Total unique titles now:", total_books(inventory))
        print("Titles:", book_titles(inventory))
    except Exception as e:
        print("Error populating inventory:", e)


def scenario_member_borrows(inventory, members, transactions):
    """Member M100 (Alice) borrows '1984'."""
    print("\n--- Scenario: Member borrows a book ---")
    # Find '1984' ISBN via search (simulate staff lookup)
    hits = search_books(inventory, "1984")
    if not hits:
        print("Book '1984' not found in inventory.")
        return
    isbn = hits[0].get("isbn")
    member_id = "M100"

    try:
        # Validate membership & ISBN
        status = check_membership(members, member_id)
        print(f"Member {member_id} status:", status)
        if status != "Active":
            print("Member not active; cannot checkout.")
            return

        if not validate_isbn(isbn):
            print("Invalid ISBN for the requested book.")
            return

        # Create a checkout transaction
        checkout_date = date(2025, 10, 1)
        transactions.append({"isbn": isbn, "member_id": member_id, "action": "checkout", "date": checkout_date.isoformat()})
        print(f"Member {member_id} checked out ISBN {isbn} on {checkout_date}")

        # Calculate due date for the checkout
        due = calculate_due_date(checkout_date, 14)
        print("Calculated due date:", due)
    except Exception as e:
        print("Error during borrow flow:", e)


def scenario_return_and_overdue(inventory, transactions):
    """Process a late return and detect overdue items for notifications."""
    print("\n--- Scenario: Return processing & overdue detection ---")
    # Simulate return by M100 happening late
    try:
        # Member returns one book late (assume original checkout on 2025-10-01)
        return_date = date(2025, 10, 20)  # late return (due was 2025-10-15)
        # Find the checkout transaction to return (simple ledger scan)
        for tx in transactions:
            if tx["action"] == "checkout":
                # Append a return transaction
                transactions.append({"isbn": tx["isbn"], "member_id": tx["member_id"], "action": "return", "date": return_date.isoformat()})
                print(f"Processed return for member {tx['member_id']} on {return_date} (ISBN {tx['isbn']})")
                break

        # Detect overdue books as of a date (e.g., 2025-10-20)
        current = date(2025, 10, 20)
        overdue_list = overdue_books(transactions, current.isoformat())
        if overdue_list:
            print("Overdue items detected:", overdue_list)
            # For demo, send notifications for any overdue items
            for item in overdue_list:
                member = item.get("member_id", "UNKNOWN")
                title = item.get("title", item.get("isbn", "Unknown"))
                print(f"Sending overdue notification to {member} for {title}")
                send_overdue_notification(member, title)
        else:
            print("No overdue items found at this time.")
    except Exception as e:
        print("Error during return/overdue flow:", e)


def scenario_fines_and_updates(members, transactions):
    """Compute fines for an overdue transaction and update member or book info if needed."""
    print("\n--- Scenario: Compute fines & update records ---")
    try:
        # For demo, compute fine for 5 overdue days
        days_overdue = 5
        amount = fine_amount(days_overdue)
        print(f"Computed fine for {days_overdue} days overdue: ${amount:.2f}")

        # Example of updating book info after staff notices missing metadata
        print("Updating book metadata example (no-op if not found)...")
        # This demo does not have direct access to inventory here; in practice staff would call update_book_info.
    except Exception as e:
        print("Error computing fines or updating records:", e)


def scenario_staff_tasks(inventory):
    """Staff-run operations like searching, removing, and reporting."""
    print("\n--- Scenario: Staff tasks & reporting ---")
    try:
        # Staff searches for all books by 'Orwell'
        print("Searching for 'Orwell':", search_books(inventory, "Orwell"))

        # Staff removes a deprecated/damaged copy (by ISBN)
        remove_isbn = "9780143127741"
        removed = remove_books(inventory, remove_isbn)
        print(f"Attempted to remove ISBN {remove_isbn}: Removed = {removed}")
        print("Inventory titles now:", book_titles(inventory))
    except Exception as e:
        print("Error during staff tasks:", e)


def run_scenario():
    print("=== Scenario-Based Library Demo ===")
    inventory, members, transactions = setup_library()

    # Step 1: Populate inventory (library opening)
    scenario_populate_inventory(inventory)

    # Step 2: Member borrows a book
    scenario_member_borrows(inventory, members, transactions)

    # Step 3: Staff tasks (search & remove a copy)
    scenario_staff_tasks(inventory)

    # Step 4: Return processing & overdue detection/notifications
    scenario_return_and_overdue(inventory, transactions)

    # Step 5: Compute fines and simulate record update
    scenario_fines_and_updates(members, transactions)

    # Final summary
    try:
        print("\n--- Final Summary ---")
        print("Total unique books:", total_books(inventory))
        print("Titles remaining:", book_titles(inventory))
        print("Total currently checked out (computed from transactions):", books_checked_out(transactions))
    except Exception as e:
        print("Error printing final summary:", e)

    print("\n=== End Scenario ===")


if __name__ == "__main__":
    run_scenario()
