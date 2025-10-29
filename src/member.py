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
