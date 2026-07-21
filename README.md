# Personal Finance Tracker

A simple command-line finance tracking application written in Python. It allows users to create, view, and delete finance records, which are stored locally in a JSON file.

## Features

* Create income and expense records
* Record dates, amounts, categories, and descriptions
* Review a record before saving it
* View all saved finance records
* Delete all saved records
* Store data locally in JSON format
* Clear the terminal between menu screens
* Compatible with Windows, macOS, and Linux

> Update and individual record deletion options are displayed in the menu but have not yet been implemented.

## Requirements

* Python 3.8 or later
* No third-party packages are required

The program only uses Python standard-library modules:

* `json`
* `os`

The `datetime` module is currently imported but is not used.

## Installation

Clone or download the project files:

```bash
git clone <repository-url>
cd <repository-folder>
```

Alternatively, place the Python file in a new folder on your computer.

## Running the Program

Run the application from a terminal:

```bash
python finance_tracker.py
```

Depending on your system, you may need to use:

```bash
python3 finance_tracker.py
```

Replace `finance_tracker.py` with the actual name of the Python file.

## Menu Options

When the program starts, it displays the following menu:

```text
1. Create Finance Record
2. View All Records
3. Update Finance Record
4. Delete Finance Record
5. Delete All Finance Records
6. Exit
```

### 1. Create Finance Record

Prompts the user to enter:

* Date in `DD-MM-YYYY` format
* Amount in pounds
* Type, such as `Income` or `Expense`
* Category
* Description

The completed record is displayed for confirmation before it is saved.

Example:

```text
Enter the date (DD-MM-YYYY): 20-07-2026
Enter the amount (£): 35.50
Enter the type (Income/Expense): Expense
Enter the category: Food
Enter a description: Weekly grocery shopping
```

### 2. View All Records

Reads the stored finance records and displays each record in the terminal.

Example output:

```text
Record 1:
Date: 20-07-2026
Amount: £35.50
Type: Expense
Category: Food
Description: Weekly grocery shopping
```

### 3. Update Finance Record

This option is not currently implemented.

### 4. Delete Finance Record

This option is not currently implemented.

### 5. Delete All Finance Records

Asks for confirmation and then removes all stored finance records.

This action cannot be undone.

### 6. Exit

Closes the application.

## Data Storage

Finance records are stored in:

```text
Tracked_Finances.JSON
```

The file is created automatically in the current working directory after the first record is saved.

Example file contents:

```json
[
    {
        "date": "20-07-2026",
        "amount": 35.5,
        "type": "Expense",
        "category": "Food",
        "description": "Weekly grocery shopping"
    },
    {
        "date": "21-07-2026",
        "amount": 1200.0,
        "type": "Income",
        "category": "Salary",
        "description": "Monthly salary payment"
    }
]
```

Do not manually edit the file while the program is running.

## Project Structure

```text
project-folder/
├── finance_tracker.py
├── Tracked_Finances.JSON
└── README.md
```

The JSON file will not appear until a record has been saved.

## Finance Class

The `Finance` class represents an individual finance record.

### Attributes

| Attribute     | Description                             |
| ------------- | --------------------------------------- |
| `date`        | Date associated with the record         |
| `amount`      | Monetary value of the record            |
| `type`        | Record type, normally income or expense |
| `category`    | User-defined finance category           |
| `description` | Additional details about the record     |

### Methods

| Method            | Description                              |
| ----------------- | ---------------------------------------- |
| `subtract(value)` | Subtracts a value from the record amount |
| `get_amount()`    | Returns the current amount               |
| `display()`       | Prints the record details                |
| `add_record()`    | Adds the record to the JSON file         |

## Current Limitations

* Dates are stored as text and are not validated.
* Amount input must be numeric or the program will stop with an error.
* Income and expense types are not validated.
* Update functionality is not implemented.
* Individual record deletion is not implemented.
* Records do not have unique identifiers.
* The program does not calculate totals, balances, or category summaries.
* Invalid or damaged JSON data is not handled.
* Deleting all records writes an empty JSON object rather than an empty list.

## Possible Improvements

Future versions could include:

* Date and input validation
* Error handling for invalid amounts
* Unique record IDs
* Editing existing records
* Deleting individual records
* Income, expense, and balance totals
* Filtering by category, type, or date
* Monthly financial summaries
* CSV export
* Password protection
* Automated tests
* A graphical user interface

## Important Notes

This project is intended for learning and basic personal finance tracking. It should not be treated as professional accounting or financial-management software.

Because records are stored locally without encryption, avoid using the application for sensitive financial information.

## License

This project is available for educational and personal use. Add a suitable licence file if you plan to distribute or publish it.
