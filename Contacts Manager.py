# Contacts Manager CLI Project

import csv
import os

FILENAME = "contacts.csv"

def setup_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])
    else:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) > 1:
                print("📞 Last saved contact:", rows[-1])

def add_contact():
    details = input("Enter contact in format: name, phone, email\n")
    parts = details.split(",")
    if len(parts) != 3:
        print("❌ Invalid format. Use: name, phone, email")
        return
    name, phone, email = [p.strip() for p in parts]
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print("✅ Contact saved.")

def view_contacts():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_contact():
    name = input("Enter name to search: ").strip().lower()
    found = False
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if name == row[0].strip().lower():
                print("📇 Found:", row)
                found = True
    if not found:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip().lower()
    found = False
    with open(FILENAME, "r") as file:
        rows = list(csv.reader(file))
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0].strip().lower() != name:
                writer.writerow(row)
            else:
                found = True
    if found:
        print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found to delete.")

def main():
    setup_file()
    while True:
        print("\n--- Contacts Manager ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("📴 Exiting Contacts Manager. Bye!")
            break
        else:
            print("❌ Invalid choice. Enter 1-5.")

if __name__ == "__main__":
    main()