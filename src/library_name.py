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
def validate_isbn(isbn):
    
def send_overdue_notification(member, book_title, due_date):
    notification = (
        f"{member['name']}, our records show you have not returned '{book_title}'.\n"
        f"The due date was {due_date}. To avoid further penalties, please return the book as soon as you can."
    )
    return notification
 
