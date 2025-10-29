#loan.py
#Mariam Diaby

from datetime import date

class Loan:
  def __init__(self, member_id, book_title, issue_date, due_date):
    if not member_id:
      raise ValueError("Member ID shouldn't be empty")
    if not book_title:
      raise ValueError("Book title shouldn't be empty")
    if due_date < issue_date:
      raise ValueError("Due date cannot be before issue date")

self._member_id = member_id
self._book_title = book_title
self._issue_date = issue_date
self._due_date = due_date
self._return_date = None

@property
def member_id(self):
  return self._member_id

@property
def book_title(self):
  return self._book_title

@property
def issue_date(self):
  return self._issue_date

@property
def due_date(self):
  return self._due_date

@property
def return_date(self):
  return self._return_date

@return_date.setter
def return_date(self,value):
  if value < self._issue_date:
    raise ValueError("Return date cannot be before issue date")
    self._return_date = value
