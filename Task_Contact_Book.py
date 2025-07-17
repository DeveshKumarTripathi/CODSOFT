contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print(" Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    key = input("Search by name or phone: ")
    found = False
    for contact in contacts:
        if key.lower() in contact["name"].lower() or key in contact["phone"]:
            print("\n Contact Found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
            break
    if not found:
        print(" Contact not found.\n")

def update_contact():
    phone = input("Enter the phone number of the contact to update: ")
    for contact in contacts:
        if contact["phone"] == phone:
            print("Enter new details (leave blank to keep current):")
            name = input(f"Name ({contact['name']}): ") or contact['name']
            new_phone = input(f"Phone ({contact['phone']}): ") or contact['phone']
            email = input(f"Email ({contact['email']}): ") or contact['email']
            address = input(f"Address ({contact['address']}): ") or contact['address']
            contact.update({"name": name, "phone": new_phone, "email": email, "address": address})
            print(" Contact updated successfully!\n")
            return
    print(" Contact not found.\n")

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!\n")
            return
    print(" Contact not found.\n")

def menu():
    while True:
        print("📱 CONTACT BOOK MENU")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.\n")

# Run the contact book
menu()
