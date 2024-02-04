contacts = []


def display_menu():
    print("1.Add Contact")
    print("2.Delete Contact")
    print("3.Display Contacts list ")
    print("4.Edit Contact Info")
    print()


def add_contact(name, phone_number):
    contacts.append({"Name": name.title(), "Phone Number": phone_number})


def search_for_contact_name(name):
    if contacts:
        for contact in contacts:
            if contact["Name"] == name.title():
                return f"{contact["Name"]} \t {contact["Phone Number"]}"
        return "Contact not found"
    return "There are no contacts here"


def delete_contact(name):
    for contact in contacts:
        if contact["Name"] == name.title():
            contacts.remove(contact)
            return "Contact deleted successfully"
    return "Contact not found"


def delete_contact_by_number(number):
    for contact in contacts:
        if contact["Phone Number"] == number:
            contacts.remove(contact)
            return "Contact deleted successfully"
    return "Contact not found"


def display_contacts():
    if contacts:
        for contact in contacts:
            print(f"{contact["Name"]} \t {contact["Phone Number"]}\n")
    return "There are no contacts here"


def edit_contact_name(name, new_name):
    if contacts:
        for contact in contacts:
            if contact["Name"] == name.title():
                contact["Name"] = new_name.title()


def edit_contact_number(param, new_number):
    if contacts:
        for contact in contacts:
            if contact["Name"] == param.title() or contact["Phone Number"] == param:
                contact["Phone Number"] = new_number
        return "Contact not found"
    return "There are no contacts here"


def search_for_contact_number(number: str) -> str:
    if contacts:
        for contact in contacts:
            if contact["Phone Number"] == number:
                return f"{contact["Name"]} \t {contact["Phone Number"]}"
        return "Contact not found"
    return "There are no contacts here"
