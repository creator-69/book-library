# Book Library

A Python object-oriented programming exercise modeling books, users, and a simple library.

## What's implemented

- `Boks` stores a book's author, publication year, and title, and exposes a `get_info()` method.
- `User` stores a user's name and email.
- `Library` keeps in-memory lists of books and users, with methods to add books, register users, borrow by title, and return a book.
- The script includes example objects and demonstrates borrowing and returning.

## Run

Requires Python 3.

```bash
python Library.py
```

## Learning focus

Classes, constructors, instance attributes, methods, lists of objects, and basic object interaction.

**Current limitations:** data is in memory only; borrowing does not track which user has a book, and the age-check method uses a fixed year. These are useful next steps for improving the model.
