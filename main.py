import phonebook

while True:
    phonebook.display_menu()
    reply = int(input("Select any option (1-4 )\n"))
    match reply:
        case 1:
            name = input("Enter the name of the contact:\n")
            phone_number = input("Enter phone number:\n")
            phonebook.add_contact(name, phone_number)
            print("Contact added successfully!")
            print()

        case 2:
            phonebook.display_contacts()
            name = input("Enter the name of the contact to delete: ")
            phonebook.delete_contact(name)
            phonebook.display_contacts()
            print()

        case 3:
            print("NAMES\tPHONE NUMBERS")
            print(phonebook.display_contacts())

        case 4:
            print(phonebook.display_contacts())
            option = input("Would you like to edit name or number?\n").lower()
            while option != "name" or "number":
                option = input("Would you like to edit name or number? answer 'name' or 'number'\n").lower()

            if option == "name":
                name = input("Enter name of contact you'd like to edit: ")
                new_name = input("Enter new Name: ")
                phonebook.edit_contact_name(name, new_name)
                print(phonebook.display_contacts())
            else:
                contact = input("Enter name or number of contact you'd like to edit: ")
                new_number = input("Enter new number: ")
                phonebook.edit_contact_number(contact, new_number)
                print(phonebook.display_contacts())

        case _:
            print("Invalid Input")
