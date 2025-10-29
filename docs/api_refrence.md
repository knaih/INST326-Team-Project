class Member:
    """
    Represents a library member and stores their key information.

    Parameters
    ----------
    member_id : str
        Unique identifier for the member.
    name : str
        Full name of the member.
    status : str, optional
        Account status (default "active").

    Attributes
    ----------
    _id : str
        Private identifier for the member.
    _name : str
        Member's name.
    _status : str
        Account status (default "active").
    _borrowed_books : list
        List of books currently borrowed by the member.

    Examples
    --------
    >>> m = Member("M001", "Colleen Hoover")
    >>> m.is_active()
    True
    >>> m._borrowed_books.append("It Ends With Us")
    >>> m._borrowed_books
    ['It Ends With Us']
    """

    def __init__(self, member_id, name, status="active"):
        """
        Initialize a Member object.

        Parameters
        ----------
        member_id : str
            The unique ID of the member.
        name : str
            The member's name.
        status : str, optional
            The member's account status (default "active").
        """
        self._id = member_id
        self._name = name
        self._status = status
        self._borrowed_books = []

        

    def is_active(self):
        """
        Check whether the member account is active.

        Returns
        -------
        bool
            True if the member's status is "active", False otherwise.

        Examples
        --------
        >>> m = Member("M001", "Colleen Hoover")
        >>> m.is_active()
        True
        """
        return self._status == "active"

    def notify_overdue_books(self, overdue_books):
        """
        Notify the member of overdue books.

        Parameters
        ----------
        overdue_books : list
            A list of overdue books (titles or objects).
        pass

