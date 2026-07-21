import datetime
import json
import os

class Finance:
    def __init__(self, date, amount, type, category, description):
        self.date = date
        self.amount = amount
        self.type = type
        self.category = category
        self.description = description

    def subtract(self, value):
        self.amount -= value

    def get_amount(self):
        return self.amount
    
    def display(self):
        print(f"Date: {self.date}")
        print(f"Amount: £{self.amount:.2f}")
        print(f"Type: {self.type}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
    
    def add_record(self):
        finance_data = {
            "date": self.date,
            "amount": self.amount,
            "type": self.type,
            "category": self.category,
            "description": self.description
        }
        # Read existing records
        records = []
        if os.path.exists("Tracked_Finances.JSON"):
            with open("Tracked_Finances.JSON", "r", encoding="utf-8") as f:
                data = json.load(f)
                # Convert dict to list if needed
                records = [data] if isinstance(data, dict) else data
        
        # Append new record
        records.append(finance_data)
        
        # Write updated records
        with open("Tracked_Finances.JSON", "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=4)

def create_finance_record():
    date = input("Enter the date (DD-MM-YYYY): ")
    amount = float(input("Enter the amount (£): "))
    type = input("Enter the type (Income/Expense): ")
    category = input("Enter the category: ")
    description = input("Enter a description: ")
    finance_record = Finance(date, amount, type, category, description)
    os.system('cls' if os.name == 'nt' else 'clear')
    finance_record.display()
    confirm = input("Do you want to submit this finance record? (yes/no): ")
    if confirm.lower() == "yes":
        finance_record.add_record()
        print("Finance record created successfully!")
    else:
        print("Finance record creation cancelled.")
    input("Press Enter to return to the menu...")
    os.system('cls' if os.name == 'nt' else 'clear')

def view_all_finance_records():
    print("Finance Records:")
    print("----------------------------------")
    if os.path.exists("Tracked_Finances.JSON"):
        with open("Tracked_Finances.JSON", "r", encoding="utf-8") as f:
            data = json.load(f)
            # Handle both dict (single record) and list (multiple records)
            records = [data] if isinstance(data, dict) else data
            if records:
                for i, record in enumerate(records, 1):
                    print(f"Record {i}:")
                    finance_obj = Finance(record['date'], record['amount'], record['type'], record['category'], record['description'])
                    finance_obj.display()
                    print("----------------------------------")
            else:
                print("No finance records found.")
                print("----------------------------------")
    else:
        print("No finance records found.")
        print("----------------------------------")
    input("Press Enter to return to the menu...")
    os.system('cls' if os.name == 'nt' else 'clear')

def update_finance_record():
    # Code to update a finance record in a database or API
    pass

def delete_finance_record():
    # Code to delete a finance record from a database or API
    pass

def delete_all_finance_records():
    confirm = input("Are you sure you want to delete all finance records? This action cannot be undone. (yes/no): ")
    if confirm.lower() == "yes":
        with open("Tracked_Finances.JSON", "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        print("All finance records have been deleted.")
    else:
        print("Deletion of all finance records cancelled.")
    input("Press Enter to return to the menu...")
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

def show_menu():
    print("1. Create Finance Record")
    print("2. View All Records")
    print("3. Update Finance Record")
    print("4. Delete Finance Record")
    print("5. Delete All Finance Records")
    print("6. Exit")
    choice = input("Enter your choice: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        create_finance_record()
    elif choice == "2":
        view_all_finance_records()
    elif choice == "3":
        update_finance_record()
    elif choice == "4":
        delete_finance_record()
    elif choice == "5":
        delete_all_finance_records()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to return to the menu...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        show_menu()