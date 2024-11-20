import utils
import time
from contact import Contact
from hash import HashTable

phonebook = {}
phonebookHash = HashTable(size = 15)

def add_contact():
    utils.clearScreen()

    name_parts = input("Enter the name: ").strip().title().split()

# Check if at least two words are entered
    if len(name_parts) >= 2:
        firstName = name_parts[0]
        lastName = name_parts[1]
        name = firstName + " " + lastName
        print("Name:", name)
    else:
        print("Please enter both a first and last name.")
    #firstName, lastName = input("Enter the name: ").strip().title().split(" ")
    #name = firstName + " " + lastName
    phone = input("Enter the phone number: ").strip()
    phonebook[name] = phone
    print(f"\nContact {name} added successfully.")
    while True:
        if utils.go_back() == True:
            break

def view_contacts():
    phonebookHash.display()
    utils.goBack()
    """
    while True:
        utils.clearScreen()
        if phonebook:
            print("\nPhonebook Contacts:")
            for name, phone in phonebook.items():
                print(f"{name}: {phone}")
        else:
            print("Phonebook is empty.")
        if utils.goBack() == True:
            break
    """
def search_contact():
    while True:
        utils.clearScreen()
        name = input("Enter the name to search: ").strip().title()
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print("Contact not found.")
        if utils.goBack() == True:
            break

def delete_contact():
    utils.clearScreen()
    name = input("Enter the name to delete: ").strip().title()
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")
    while True:
        if utils.goBack() == True:
            break

def test():
    utils.clearScreen()

    name_first = input("Enter the name: ").strip().title().split()

    if len(name_first) >= 1:
        firstName = name_first[0]
    lastName = input("Enter the Last Name: ").strip()
    phone = input("Enter the phone number: ").strip()
    if not lastName:
        print("First Name cannot be empty")
        utils.goBack()
        return
    if not phone:
        print("Phone Number cannot be empty")
        utils.goBack()
        return
    newContact = Contact(firstName, phone, lastName)
    phonebookHash.insert(newContact)
    print("Contact was added successfully")
   #print(newContact)
    while True:
        time.sleep(1)
        if utils.goBack():
            break