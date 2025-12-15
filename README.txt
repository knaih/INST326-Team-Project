# Library Management System - Function Library

**Team:** Bookworms
**Domain:** Library Management System  
**Course:** INST326 - Object-Oriented Programming for Information Science  

## Project Overview (Domain Focus/Problem Statement)
The project focuses on the domain of Library and Information Management. It focuses on building a system that helps librarians manage and track inventory, memberships, and events efficiently. This system aims to automate library operations such as updating inventory, tracking memberships, due dates, and event types to improve accuracy, organization, and accessibility in a library.

## Problem Statement
Librarians struggle with:
- Tracking Overdue Books
- Inaccurate Inventory(what’s in stock and out of stock)
- Managing active and inactive memberships
- Keeping track of events (private and public)

## Key OOP concepts demonstrated:
- **Inheritance**: LibraryItem → Book / AudioBook  
- **Polymorphism**: `__str__` behaves differently for each subclass  
- **Abstract Class**: AbstractLibraryItem ensures a common interface  
- **Composition**: Members have Loans, Loans contain LibraryItems  

## Installation and Setup
1. Clone this repository:
```bash
git clone https://github.com/knaih/INST326-Team-Project.git
cd INST326-Team-Project
```

2. No external dependencies required - uses Python standard library only

3. Import functions in your Python code:
```python
from src.library_functions import add_books, search_books, validate_isbn, calculate_due_date, fine_amount

## Running Tests
To run all unit, integration, and system tests, use:
```bash
python -m unittest discover

## Usage Examples For Key Functions
inventory = []
add_books(inventory, [
    {"isbn": "9780306406157", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"isbn": "9780143127741", "title": "To Kill a Mockingbird", "author": "Harper Lee"},
])

# Search for books by title or author
results = search_books(inventory, "Gatsby")
print("Search results:", results)

# Calculate due date for a borrowed book
borrow_date = date(2025, 10, 12)
due_date = calculate_due_date(borrow_date, 14)
print("Due date:", due_date)

# Compute fine for a late return
print("Fine owed: $", fine_amount(3))

# Send overdue notification to member
send_overdue_notification(member_id="M001", book_title="The Great Gatsby")
## Function Library Overview/Organization

Our library contains  15 specialized functions organized into four categories:

#### Inventory Management (7 Functions)
- `total_books()` - Count total number of books in the library
- `book_titles()` - Return a list of all book titles
- `author_name()` - Validate author name
- `add_books()` - Add any new books to the inventory
-`remove_books()` - Remove a book from the inventory using ISBN
- `update_book_info()` - Update a book's details based on ISBN
- `books_checked_out()` - Count the total number of books checked out library

#### Member Management (3 Functions)
- `check_membership()` - Verify if member is active or inactive
- `fine_amount()` - Calculate the fine for overdue books
- `calculate_due_date()` - Calculate the days due for the borrowed book

#### Library Operations/Events (5 Functions)
- `search_books()` - Search books by title, keyword, or author
- `validate_isbn()` - To check if ISBN-10 or ISBN-13 is valid
- `get_overdue_books()` - Identify books past it's due date
- `list_events_by_type()` - Type of library event
- `send_overdue_notification()` - Notify members of overdue books


## Team Roles and Contributions
Mariam Diaby: Developer and feature implementation
Kaelyn Naih: Team Lead 
Vainqueur Mukenyi: Developer 
Anyi Tasong: Developer , Member management function / Repo setup and documentaton.

## Code Review Process
- All Functions have been reviewed by one team member.


## AI Collaboration 
- Used AI to properly understand what the assignment was asking for.
- Constructed Function_Reference.
- Generated examples for us to go off of as a team.

## Video Presentation
Video Link: ()

## Repository Structure
library-management-library/
├── README.md
├── data/
│   └── library_data.json
├── src/                       
│   ├── __init__.py  
│   ├── library_items.py
│   ├── member.py
│   ├── loan.py
│   ├── persistence.py
│   ├── library.py
│   ├── event.py
│   └── library_functions.py   
├── docs/                      
│   ├── function_reference.md  
│   └── usage_examples.md      
├── examples/                  
│   └── demo_script.py         
└── requirements.txt         

## Testing Strategy

Our testing approach follows three levels of validation:

### Unit Tests
- Verify individual functions such as adding/removing books and members.
- Focus on input validation and edge cases.

### Integration Tests
- Validate interaction between modules (inventory, members, events).
- Ensure data flows correctly across components.

### System Tests
- Test complete end-to-end workflows that reflect real user actions.
- Workflows include:
  - Member registration and persistence
  - Book borrowing and inventory updates
  - Save and load system state
  - Import and export functionality

System tests are implemented in:
tests/test_system_workflows.py

### Running Tests
To run all tests:
```bash
pytest
```md
See docs/testing.md for detailed testing coverage.
