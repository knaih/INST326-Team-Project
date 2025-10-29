## Purpose
""" The Purpose of the Member function represents an individual member in the system. It stores key information in identifying a specific member id, name, status, and a list of borrowed books. 

- Responsibilities include: Initialize and store identifying data for each member, Track which books the member currently has borrowed, Check if a member’s account is active or not, (Future) Notify members about overdue books or fines.

Private attributes (recommended):
_member_id: str — unique identifier for the member (immutable after creation).
_name: str — full name.
_email: str — contact email.
_phone: Optional[str] — contact phone number.
_join_date: datetime.date — date the member joined.
_status: str — one of ("active", "suspended", "closed").
_outstanding_loans: List[Loan] — list of Loan objects currently checked out by this member.
_fines_due: Decimal — total fines outstanding.

Public properties (with validation):
member_id (read-only)
name (read/write) — non-empty string
email (read/write) — validated (basic pattern)
phone (read/write) — optional, basic normalization
join_date (read-only)
status (read/write) — allowed values only
fines_due (read-only) — Decimal

Instance methods (3–5 recommended):
borrow_item(item, loan_manager, due_date=None) -> Loan — attempt to borrow an item; delegates to loan manager / Catalog functions. Returns created Loan.
return_item(loan, return_date=None) -> dict — close the loan; compute fines if overdue; update _outstanding_loans and _fines_due.
is_overdue() -> bool — true if any outstanding loan is past its due date.
outstanding_items() -> List[Item] — list of items currently checked out.
to_dict() -> dict — serializable representation for storage / API responses.

Magic methods:
__str__ — human-friendly summary (e.g., "Member: <id> — <name> (<status>)").
__repr__ — unambiguous constructor-like representation.
Docstrings and examples: Each public class and method MUST include a docstring in the NumPy or Google style (the repo uses simple triple-quoted docstrings). Examples should be short and run-able.

"""
