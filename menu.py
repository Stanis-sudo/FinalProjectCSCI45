import utils

phonebook = {}

def add_contact():
    utils.clear_screen()
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    phonebook[name] = phone
    print(f"\nContact {name} added successfully.")
    while True:
        if utils.go_back() == True:
            break

def view_contacts():
    while True:
        utils.clear_screen()
        if phonebook:
            print("\nPhonebook Contacts:")
            for name, phone in phonebook.items():
                print(f"{name}: {phone}")
        else:
            print("Phonebook is empty.")
        if utils.go_back() == True:
            break

def search_contact():
    while True:
        utils.clear_screen()
        name = input("Enter the name to search: ")
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print("Contact not found.")
        if utils.go_back() == True:
            break

def delete_contact():
    utils.clear_screen()
    name = input("Enter the name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")
    while True:
        if utils.go_back() == True:
            break
