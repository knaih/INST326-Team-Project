# System Workflow Test Plan

This document outlines the end-to-end workflows tested in our Library
Management System. These workflows reflect real user interactions and
verify full system integration, including persistence.

## Workflow 1: Member Registration and Persistence
- Register a new member
- Save system state
- Reload system
- Verify member data persists

## Workflow 2: Book Inventory Management
- Add books to inventory
- Remove a book
- Verify inventory updates correctly

## Workflow 3: Borrow Book Workflow
- Register member
- Add book to inventory
- Borrow book
- Verify inventory count decreases
- Verify member borrowing record updates

## Workflow 4: Save and Load Full System
- Perform multiple operations
- Save system state to file
- Load system state
- Verify all data is restored correctly

## Workflow 5: Export Report
- Generate inventory or member report
- Export to file
- Verify exported file contents
