#loan.py

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

def receipt_line(self):
  return f"{self._book_title} - due {self._due_date.strftime('%Y-%m-%d')}"

def mark_returned(self, return_date):
  self.return_date = return_date

def is_overdue(self, current_day):
  if self._return_date:
    return self._return_date > self._due_date
    return current_day > self._due_date

def days_late(self, current_day):
  if not self.is_overdue(current_day):
    return

  if self._return_date is not None:
    return (self._return_date - self._due_date).days

  return (current_day - self._due_date).days

def __str__(self):
  status = (
    f"Returned on {self._return_date}"
    if self._return_date
    else f"Due on {self._due_date}"
  )
  return f"{self._book_title} (Member: {self._member_id}) - {status}"

def __repr__(self):
  return f"Loan({self._member_id}, {self._book_title}, {self._issue_date}, {self._due_date})"
  
