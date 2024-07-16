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
    