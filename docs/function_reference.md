# Library Management Guide

This document provides comprehensive reference information for all functions in the Library Management. Each function includes its purpose, parameters, and return value.

## Table of Contents 
1. Inventory Management
2. Member Management
3. Library Operations/Events

# INVENTORY MANAGEMENT 
1. total_books()
Purpose: Returns the total number of books in the library inventory.
Parameters: None
Returns: int - The count of all books currently in the system

2.book_titles()
Purpose: Retrieves a list of all book titles available in the library.
Parameters:None
Returns: list[str] - A list of all book titles. 

3. author_name(name: str)
Purpose: Validates whether the provided author name is in the correct format.
Parameters:
- name(str): The author's name to validate.
Returns: bool - True if valid, otherwise False.

4.add_books(book_info: dict)
Purpose: Adds new books to the library's inventory.
Parameters: 
- book_info(dict): A dictionary containing details like title, author, ISBN and category.
Returns: None

5. remove_books(isbn: str)
Purpose: Removes a book from the iventory using its ISBN.
Parameters:
- ISBN(STR): The ISBN of the book to remove.
Returns: bool - True if the book was successfully removed, False otherwise

6. update_book_info(isbn: str, new_info:dict)
Purpose: Updates the information for a book already in the inventory.
Parameters:
- ISBN(str): The ISBN of the book to update. New_info(dict): The updated book details.
Returns: bool - True if update succeeded, otherwise False.

7. books_checked_out()
Purpose: Counts the total number of books that are currently checked out from the library.
Parameters: None
Returns: int - Number of checked-out books. 

# Member Management
1. check_membership(memver_id: str)
Purpose:
- Verifies whether a member's account is active or inactive.
Returns:
- str - "Active" or "Inactive" based on membership status.

2. fine_amount(days_overdue: int)
Purpose:
- Calculates the fine for overdue books.
Parameters:
- days_overdue(int): The number of days a book is overdue.
Returns:
- float - The fine amount(e.g., $0.25 per day).

3. calculate_due_date(borrow_date: str, loan_period: int)
Purpose:
- Determines the due date for a borrowed book.
Parameters:
- borrow_date (str): The date the book was borrowed(example: "2025-10-08").
Returns:
- str - The calculated due date.

# Library Operations / Events 
1. search_books(keyword: str)
Purpose:
- Searches for books by title, keyword, or author.
Parameters:
- keyword(str): The search term used to find books.
Returns:
- list[dict] - A list of books matching the search criteria.

2. Validate_isbn(isbn: str)
Purpose:
- Checks if an ISBN-10 or ISBN-13 is valid.
Parameters:
- ISBN(str): The ISBN to validate.
Returns:
bool - True if the ISBN is valid, otherwise False.

3. Overdue_books(current_date: str)
Purpose:
- Identifies books that are past their due date.
Parameters:
- Current_date(str): The current date to compare against due dates.
Returns:
- list[dict] - A list of overdue books.

4. event_type(event_name: str)
Purpose:
- Defines the type of library event (ex: "Book Club," "Author Talk,""Workshop.").
Parameters:
- event_name(str): The event name.
Returns:
- str - The event categpry or type.

5. send_overdue_notification(memver_id: str, book_title: str)
Purpose:
- Sends a notification to members with overdue books.
Parameters:
- Member_id(str): The member receiving the notification.
- book_title(str): The title of the overdue book.
Returns:
- None.



# General Usage Notes
Function Inputs:
- Most functions expect lists of dictionaries(for inventory) or dictionaries(for members). Stick to consistent key namingStick to consistent key naming ("isbn", "title", "author", "active").

Data Format:
- Use ISO-formatted dates (YYYY-MM-DD) for portability.
- For numerical data (e.g., fines), prefer floats but format to 2 decimals before display.

Reusability:
- Functions are modular — they can be imported individually or together.
- Each function’s return value is designed to be chainable (e.g., output from search_books() can be passed to book_titles()).

Performance:
 - Most functions run in linear time (O(n)), suitable for small–medium library databases (<10,000 records).
- If scaling beyond that, consider indexing or database-backed queries in future versions.
