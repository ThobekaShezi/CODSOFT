import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Thobeka's Contact Book")

        self.contacts = []

        self.name_label = tk.Label(root, text="Contact name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone number:")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        # added my buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # added a listbox to display contacts on the side
        self.contacts_listbox = tk.Listbox(root)
        self.contacts_listbox.grid(row=0, column=2, rowspan=9, padx=10, pady=5)

        # implemented a grid layout
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)

        # added code to clear entry fields after contact has been addded successfully
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

        self.update_contacts_listbox()
        messagebox.showinfo("Contact Manager", f"Contact {name} added successfully \u2713")

    def view_contacts(self):
        self.update_contacts_listbox()

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term is not None:
            results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]

            if not results:
                messagebox.showinfo("Contact Manager", "No matching contacts found.")
            else:
                contact_list = "\n".join([f"{contact.name} - {contact.phone}" for contact in results])
                messagebox.showinfo("Contact Manager - Search Results", contact_list)

    def update_contact(self):
        selected_contact_index = self.contacts_listbox.curselection()

        if not selected_contact_index:
            messagebox.showinfo("Contact Manager", "Please select a contact.")
            return

        selected_contact_index = int(selected_contact_index[0])
        selected_contact = self.contacts[selected_contact_index]

        # Display a simple dialog for updating phone number
        new_phone = simpledialog.askstring("Update Contact", f"Enter new phone (current: {selected_contact.phone}):", initialvalue=selected_contact.phone)

        if new_phone is not None:
            selected_contact.phone = new_phone
            self.update_contacts_listbox()
            messagebox.showinfo("Contact Manager", "Contact updated successfully.")

    def delete_contact(self):
        selected_contact_index = self.contacts_listbox.curselection()

        if not selected_contact_index:
            messagebox.showinfo("Contact Manager", "Please select a contact.")
            return

        selected_contact_index = int(selected_contact_index[0])
        deleted_contact = self.contacts.pop(selected_contact_index)

        self.update_contacts_listbox()
        messagebox.showinfo("Contact Manager", f"Contact deleted successfully: {deleted_contact.name}")

    def update_contacts_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactScreen(root)
    root.mainloop()
