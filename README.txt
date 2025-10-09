# Library Management System - Function Library

**Team:** Bookworms
**Domain:** Library Management System  
**Course:** INST326 - Object-Oriented Programming for Information Science  

## Project Overview (Domain Focus/Problem Statement)
The project focuses on the domain of Library and Information Management. It focuses on building a system that helps librarians manage and track inventory, memberships, and events efficiently. This system aims to automate library operations such as updating inventory, tracking memberships, due dates, and event types to improve accuracy, organization, and accessibility in a library.

## Problem Statement
Librarians struggle with:
Tracking Overdue Books
Inaccurate Inventory(what’s in stock and out of stock)
Memberships are not being paid for
Keep track of events (private and public)

## Installation and Setup
1. Clone this repository:
```bash
git clone https://github.com/knaih/INST326-Team-Project/tree/main
cd
```

2. No external dependencies required - uses Python standard library only

3. Import functions in your Python code:
```python
from [] import add_books, search_books, validate_isbn

## Usage Examples For Key Functions

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
- `overdue_books()` - Identify books past it's due date
- `event_type()` - Type of library event
- `send_overdue_notification()` - Notify members of overdue books


## Team Roles and Contributions
Mariam Diaby: 
Kaelyn Naih: 
Vainqueur Mukenyi: 
Anyi Tasong:
