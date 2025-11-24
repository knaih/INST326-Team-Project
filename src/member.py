class Member:
  def__init__(self, member_id, name, status="active"):
    self._if = member_id
    self._name = name
    self._status = status
    self._borrowed_books = []

  def is_active(self):
    return self._status == "active"

  def notify_overdue_books(self, overdue_books):
    pass 


from loan import Loan

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.loans = []     # composition → Member HAS-A list of Loans

    def add_loan(self, loan):
        self.loans.append(loan)

    def remove_loan(self, loan):
        self.loans.remove(loan)
