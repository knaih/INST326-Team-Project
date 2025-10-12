#Kaelyn Naih
# Function to get overdue books
def get_overdue_books(library_records, current_day):
    overdue_books = []
    for record in library_records:
        if record['due_date'] < current_day:
            overdue_books.append(record['title'])
    return overdue_bookss

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
total_books
add_books
remove_books
search_books
