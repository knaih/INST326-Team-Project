def test_full_borrow_and_persist_workflow(tmp_path):
    # 1. Setup test environment
    library = LibrarySystem()

    # 2. Add a member
    library.add_member("001", "Alice")
    
    # 3. Add books
    library.add_book("0001", "Python 101", copies=3)

    # 4. Borrow a book
    library.borrow_book("001", "0001")

    # 5. Save state
    save_file = tmp_path / "state.json"
    library.save_system(save_file)

    # 6. Reload
    new_lib = LibrarySystem.load_system(save_file)

    # 7. Verify persistence
    assert new_lib.get_member("001").has_borrowed("0001")
    assert new_lib.get_available_copies("0001") == 2
