from rich.console import Console
import json

console = Console()


class ContactManager:

    def __init__(self):
        self.contacts = {}
        try:
            self.load_contact()
        except FileNotFoundError:
            self.save_contact()

    def save_contact(self):
        with open("contacts.json", "w") as f:
            f.write(json.dumps(self.contact))

    def load_contact(self):
        with open("contacts.json", "r") as f:
            self.contact = json.loads(f.read())
        
    def add_contact(self, name, phone, email=None, address=None):
        if name in self.contacts:
            console.print(f"[yellow]{name} is already in the contact list.[/yellow]", end="\n\n", style="bold")
            return
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        self.save_contact()
        console.print(f"[green]{name} has been added to the contact list.[/green]", end="\n\n", style="bold")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contact()
            console.print(f"[red]{name} has been removed from the contact list.[/red]", end="\n\n", style="bold")
        else:
            console.print(f"[yellow]{name} is not in the contact list.[/yellow]", end="\n\n", style="bold")

    def list_contacts(self):
        i = 1
        for name, contact in self.contacts.items():
            console.print(f"{i}. [green]{name} : [/green](phone: {contact['phone']}) - (email: {contact['email']}) - (address:  {contact['address']})", style="bold")
            i += 1
        else:
            console.print(f"[yellow]Contact list is empty.[/yellow]", style="bold")
        console.print('', end="\n\n")

    def update_contact(self, name):
        if name in self.contacts:
            phone = self.get_input("Enter phone: ", force=True)
            email = self.get_input("Enter email (Optional): ")
            address = self.get_input("Enter address (Optional): ")
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            self.save_contact()
            console.print(f"[green]{name} has been updated successfully.[/green]", end="\n\n", style="bold")
        else:
            console.print(f"[yellow]{name} not found.[/yellow]", style="bold")

    def search_contact(self, query):
        finds = []
        for key in self.contacts:
            if query in key:
                finds.append(key)
        
        if finds:
            for name in finds:
                console.print(f"[green]{name} : [/green]({self.contact[name]['phone']}) - ({self.contact[name]['email']}) - ({self.contact[name]['address']})", style="bold")
        else:
            console.print(f"[yellow]No contact found.[/yellow]", style="bold")
        console.print('', end="\n\n")

    @staticmethod
    def get_input(message, force=False):
        value = input(message)
        if force and not value:
            return ContactManager.get_input(message, force)
        return value if value else None
    
    def menu(self):
        console.print("[magenta]Contact Manager[/magenta]", style="bold")
        console.print("1. Add Contact")
        console.print("2. Remove Contact")
        console.print("3. Update Contact")
        console.print("4. List Contact")
        console.print("5. Search Contact")
        console.print("6. Exit")
        choice = int(self.get_input("Enter your choice: ", force=True))
        if choice == 1:
            name = self.get_input("Enter name: ", force=True)
            phone = self.get_input("Enter phone: ", force=True)
            email = self.get_input("Enter email (Optional): ")
            address = self.get_input("Enter address (Optional): ")
            self.add_contact(name, phone, email, address)
            self.goto_menu()
        elif choice == 2:
            name = self.get_input("Enter name: ", force=True)
            self.remove_contact(name)
            self.goto_menu()
        elif choice == 3:
            name = self.get_input("Enter name: ", force=True)
            self.update_contact(name)
            self.goto_menu()
        elif choice == 4:
            self.list_contacts()
            self.goto_menu()
        elif choice == 5:
            query = self.get_input("Enter query: ", force=True)
            self.search_contact(query)
            self.goto_menu()
        elif choice == 6:
            console.print("[green]GoodBye![/green]", end="\n\n", style="bold")
            exit()
        else:
            console.print('[red]Inmvalid input![/red]', end="\n\n", style="bold")
            self.goto_menu()

    def goto_menu(self):
        goto = self.get_input("Enter 'q' to exit or any other key to go to menu: ")
        if goto == "q":
            exit()
        else:
            self.menu()


contact_manager = ContactManager()
contact_manager.menu()
    