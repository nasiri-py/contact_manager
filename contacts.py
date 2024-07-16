from rich.console import Console

console = Console()


class ContactManager:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email=None, address=None):
        if name in self.contacts:
            console.print(f"[yellow]{name} is already in the contact list.[/yellow]", end="\n\n", style="bold")
            return
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        console.print(f"[green]{name} has been added to the contact list.[/green]", end="\n\n", style="bold")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
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
    