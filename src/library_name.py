#Kaelyn Naih
# Function to get overdue books
def get_overdue_books(library_records, current_day):
    overdue_books = []
    for record in library_records:
        if record['due_date'] < current_day:
            overdue_books.append(record['title'])
    return overdue_books

# Function to check membership
def check_membership(member_id, members_list):
    for member in members_list:
        if member['id'] == member_id:
            return member['status'] == 'active'
    return False

# Function to calculate fine
def calculate_fine(due_date, return_date, rate_per_day=0.5):
    overdue_days = return_date - due_date
    if overdue_days > 0:
        fine = overdue_days * rate_per_day
    else:
        fine = 0
    return fine

# Function to list events by type
def list_events_by_type(events_list, event_type):
    matching_events = []
    for event in events_list:
        if event['type'] == event_type:
            matching_events.append(event['name'])
    return matching_events



#Mariam
def total_books(library):
    return len(library)

def add_books(library, title, authot, isbn):
    new_nook = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }
    library.append(new_book)
    return library

def remove_books(library, isbn):
    for book in library:
        if book["isbn"] == isbn:
            library.remove(book)
            return True
    return False

def search_books(library, keyword):
    keyword = keyword.lower()
    results = [
        book for book in library
        if keyword in book["title"].lower() or keyword in book["author"].lower()
    ]
    return results


#Vainqueur
def issue_books(library, library_records, isbn, member, issue_date, due_date):
    if member['status'] != 'active':
        return f"Member {member['name']} is inactive.
        
    for book in library:
        if book['isbn'] == isbn:
        if not book['available']:
                return f"The book '{book['title']}' is currently not available."

        record = {
                'member_id': member['id'],
                'title': book['title'],
                'isbn': book['isbn'],
                'issue_date': issue_date,
                'due_date': due_date
            }
            library_records.append(record)
            return f"Book '{book['title']}' has been issued to {member['name']}."

        return "Book currently unavailable


def update_book_info(library, isbn, updated_book):
    for book in library:
        if book.get("isbn") == isbn:
            book.update(update_book)
            return True
        return False

def validate_isbn(isbn, year):
    isbn = isbn.replace("-", "").replace(" ", "")
    
    if year <= 2006:
        if len(isbn) != 10:
            return False
    elif year >= 2007:
        if len(isbn) != 13:
            return False
    
    return True
         
def send_overdue_notification(member, overdue_books):
    if not overdue_books:
        return None
    
    book_list = ""
    for book in overdue_books:
        book_list += f"{book['title']} (due on {book['due_date']})\n"
        
    notification = (
        f"{member['name']}, \n\n"
        f" our records show you have not returned the following.\n"
        f"{book_list}\n\n"
        f"The due date was {due_date}. To avoid further penalties, please return the book as soon as you can."
    )
    return notification
 
#Anyi 
def book_titles(inventory: list) -> list:
    if not isinstance(inventory, list):
        raise TypeError("Inventory must be provided as a list of dictionaries.")

titles = []
for book in inventory:
    if not isinstance(book, dict):
        raise TypeError("Each inventory item must be a dictionary.")
    if "title" not in book:
        raise KeyError("Missing 'title' key in one of the book entries.")
    titles.append(book["title"])

return titles

def author_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("Author name must be a string.")

    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Author name cannot be empty.")

    # Allow alphabetic characters, spaces, and periods
    import re
    if not re.match(r"^[A-Za-z\s\.\-]+$", cleaned):
        raise ValueError("Author name contains invalid characters.")

    # Return normalized title-cased version
    return cleaned.title()

def fine_amount(days_overdue: int, rate_per_day: float = 0.50) -> float:
     if not isinstance(days_overdue, (int, float)):
        raise TypeError("Days overdue must be an integer or float.")
    if not isinstance(rate_per_day, (int, float)):
        raise TypeError("Rate per day must be a number.")
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative.")

    return round(days_overdue * rate_per_day, 2)
    
