import csv


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def list_contact(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
            break

    def find_contact(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
            else:
                self._not_found()
            break

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def update(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                name = str(input('Input Name: '))
                phone = str(input('Input Phone: '))
                email = str(input('Input Email: '))
                contact = Contact(name, phone, email)
                self._contacts[idx] = contact
                self.save()

    def _print_contact(self, contact):
        print("""
		---*---*---*---*---*---*---*---*---\n
			Name: {}\n
			Phone: {}\n
			Email: {}\n
		---*---*---*---*---*---*---*---*---\n
		""".format(contact.name, contact.phone, contact.email))

    def _not_found(self):
        print(
            """
					---*---*---*---*---*---*---*---*---\n
					Contact not found\n
					---*---*---*---*---*---*---*---*---\n
					""")


def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input(
            """ 
			[a]dd contact
			[u]pdate contact
			[f]ind contact
			[d]elete contact
			[l]ist contacts
			[e]xit

			"""
        ))

        if command == 'a':
            name = str(input('Input Name: '))
            phone = str(input('Input Phone: '))
            email = str(input('Input Email: '))
            contact_book.add(name, phone, email)

        elif command == 'f':

            name = str(input('Input Name: '))
            contact_book.find_contact(name)

        elif command == 'u':
            name = str(input('Input Name: '))
            contact_book.update(name)

        elif command == 'd':
            name = str(input("Input Name: "))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.list_contact()

        elif command == 'e':
            break

        else:
            print("Command not found")


if __name__ == '__main__':
    run()
