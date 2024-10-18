class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update_contact(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact for {contact.name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No contact found with that name or phone number.")

    def update_contact(self, search_term):
        contact = self._find_contact(search_term)
        if contact:
            print("Enter new details (leave blank to keep current):")
            name = input(f"Name [{contact.name}]: ") or contact.name
            phone = input(f"Phone [{contact.phone}]: ") or contact.phone
            email = input(f"Email [{contact.email}]: ") or contact.email
            address = input(f"Address [{contact.address}]: ") or contact.address
            contact.update_contact(name=name, phone=phone, email=email, address=address)
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self, search_term):
        contact = self._find_contact(search_term)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact for {contact.name} deleted successfully!")
        else:
            print("Contact not found!")

    def _find_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                return contact
        return None

def user_interface():
    contact_book = ContactBook()
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_interface()
