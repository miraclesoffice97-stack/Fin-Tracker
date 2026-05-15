# FinTracker 💰

A CLI-based personal finance tracker built with Python. FinTracker lets you record income and expenses, track your balance, and view your full activity history — all from the terminal.

Originally built with JSON file storage, the project has since been upgraded to use **SQLite** as the database backend for more reliable and structured data persistence.


## Features

- **User Authentication 🔐** — Sign up and log in with username and password validation. Credentials are stored securely in a local SQLite database.

- **Income & Expense Recording** — Record income and expenses with automatic timestamping. Each transaction is saved to the database instantly.

- **Dashboard 🧾** — View your total income, total expenses, and available balance at a glance.

- **Activity History** — Browse a full log of past transactions with date and time recorded for each entry.

- **SQLite Database Integration** — Moved from JSON file storage to SQLite for structured, persistent, and reliable data management across sessions.


## Tech Stack

- Python 3
- SQLite3 (built-in)
- OOP architecture across multiple files
- datetime module for transaction timestamps


## Project Structure

```
FinTracker/
├── FintrackerAcc.py        # Handles user auth (sign up, login)
├── FintrackerMain.py       # Main app logic (income, expenses, dashboard, history)
├── sqldb.py                # Database layer — all SQLite connection and queries live here
└── Fintracker_database.db  # SQLite database file (auto-created on first run)
```


## How To Run

```bash
python3 FintrackerAcc.py
```

1. Select **1** to create a new account
2. Select **2** to log in to an existing account
3. Once logged in:
   - **1** → Dashboard (balance overview)
   - **2** → Record income
   - **3** → Record expenses
   - **4** → View activity history
   - **5** → Log out
   - **6** → Exit


## What I Learned

- Data persistence with JSON (v1) and SQLite (v2)
- Writing and executing raw SQL from Python using `sqlite3`
- Designing a database layer (`sqldb.py`) as a separate module
- OOP across multiple files with class inheritance
- Debugging real database issues — NULL handling, cursor management, and data flow between Python and SQL
- How to upgrade a working project to a new storage backend without breaking existing logic


## Version History

| Version | Storage | Notes |
|---------|---------|-------|
| v1 | JSON files | Initial build |
| v2 | SQLite database | Upgraded for structured data persistence |


## Author

Miracle DC 🗿  
Self-taught Python developer — Lagos, Nigeria  
Building from the terminal up 😎
