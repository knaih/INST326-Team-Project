# src/persistence.py
import json
from pathlib import Path

# -------------------------
# SAVE SYSTEM STATE
# -------------------------
def save_data(data, filename="data/library_data.json"):
    """
    Saves the current system state to a JSON file.
    Expects data as a dictionary: {"books": [...], "members": [...], "events": [...]}
    """
    try:
        path = Path(filename)
        path.parent.mkdir(exist_ok=True)  # Ensure data folder exists
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data: {e}")


# -------------------------
# LOAD SYSTEM STATE
# -------------------------
def load_data(filename="data/library_data.json"):
    """
    Loads the system state from a JSON file.
    Returns a dictionary with keys: books, members, events
    If file is missing or corrupted, returns empty data structure.
    """
    path = Path(filename)
    if not path.exists():
        print("No save file found. Starting with empty data.")
        return {"books": [], "members": [], "events": []}

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            # Ensure all keys exist
            return {
                "books": data.get("books", []),
                "members": data.get("members", []),
                "events": data.get("events", [])
            }
    except json.JSONDecodeError:
        print("Save file is corrupted. Starting with empty data.")
        return {"books": [], "members": [], "events": []}
    except IOError as e:
        print(f"Error loading data: {e}")
        return {"books": [], "members": [], "events": []}


# -------------------------
# EXPORT REPORTS
# -------------------------
def export_books(books, filename="data/books_report.txt"):
    """
    Exports a simple text report of all books.
    books should be a list of dictionaries or objects with __str__ implemented.
    """
    try:
        path = Path(filename)
        path.parent.mkdir(exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            for book in books:
                # If book is an object, try str(book)
                try:
                    file.write(str(book) + "\n")
                except Exception:
                    file.write(f"{book}\n")
        print(f"Books report exported to {filename}")
    except IOError as e:
        print(f"Error exporting books: {e}")


# -------------------------
# IMPORT DATA
# -------------------------
def import_books(filename):
    """
    Imports books from a JSON file.
    Returns a list of books, empty list if error.
    """
    path = Path(filename)
    if not path.exists():
        print(f"File {filename} not found. Import failed.")
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            print(f"Unexpected format in {filename}. Expected a list of books.")
            return []
    except json.JSONDecodeError:
        print(f"File {filename} is corrupted or not valid JSON.")
        return []
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return []
