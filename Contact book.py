class PriyanshuContacts:
    def __init__(self):
        self.contacts = {}

    def load_contacts(self):

        pass

    def save_contacts(self):

        pass

    def add_contact(self):
        """Add a new contact."""
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone number: ").strip()
        email = input("Enter contact email: ").strip()
        address = input("Enter contact address: ").strip()
        
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        
        print("Contact added successfully!")

    def view_contacts(self):
        """Display a list of all contacts."""
        if not self.contacts:
            print("No contacts found.")
            return
        
        print("\nContacts List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self):
        """Search for a contact by name or phone number."""
        search_term = input("Enter the name or phone number to search: ").strip()
        
        found = False
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                print(f"\nName: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                found = True
        
        if not found:
            print("No contact found with that name or phone number.")

    def update_contact(self):
        """Update an existing contact."""
        name = input("Enter the name of the contact to update: ").strip()
        
        if name not in self.contacts:
            print("Contact not found.")
            return
        
        print(f"Updating contact: {name}")
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()
        address = input("Enter new address (leave blank to keep current): ").strip()
        
        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email
        if address:
            self.contacts[name]['address'] = address
        
        print("Contact updated successfully!")

    def delete_contact(self):
        """Delete a contact."""
        name = input("Enter the name of the contact to delete: ").strip()
        
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_manager = PriyanshuContacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            contact_manager.add_contact()
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            contact_manager.search_contact()
        elif choice == '4':
            contact_manager.update_contact()
        elif choice == '5':
            contact_manager.delete_contact()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
