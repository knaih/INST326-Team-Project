""" Basic Usage example for Member Class
 by Anyi Tasong 
 """
from member import Member

m = Member("M001", "Colleen Hoover")

print(m.is_active())   #True 
print(m._name)        # Colleen Hoover 

m._status = "inactive"
print(m.is_active())   # False

m._borrowed_books.append("Verity")
m._borrowed_books.append("It Ends With Us")

print(m._borrowed_books)
# ['Verity', 'It Ends With Us']


m.notify_overdue_books(["Verity"])
# Does nothing yet, but could later send an email or print a message


""" Basic Usage example for blank 
by blank
"""

""" Basic Usage example for blank 
by blank
"""



""" Basic Usage example for blank 
by blank
"""
