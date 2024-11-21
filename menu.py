import utils
import time
from contact import Contact
from hash import HashTable

phonebook = {}
phonebookHash = HashTable(size = 3)
phonebookHash.load()

def add_contact():

    utils.clearScreen()

    name_first = input("First Name:                                 ").strip().title().split() or None
    if name_first is not None:
        firstName = name_first[0]
    else:
        utils.clearScreen()
        print("Error!\nFirst Name cannot be empty")
        utils.goBack()
        return
    
    name_middle = input("Middle Name (To skip press Enter):          ").strip().title().split() or None
    if name_middle is not None:
            middleName = name_middle[0]
    else: middleName = None

    name_last = input("Last Name (To skip press Enter):            ").strip().title().split() or None
    if name_last is not None:
        lastName = name_last[0]
    else: lastName = None
    
    inputPhone = input("Phone Number:                               ").strip().split() or None
    if inputPhone is not None:
        phone = inputPhone[0]
    else:
        utils.clearScreen()
        print("Error!\nPhone Number cannot be empty")
        utils.goBack()
        return

    inputEmail = input("Email Address (To skip press Enter):        ").strip().lower().split() or None
    if inputEmail is not None:
            email = inputEmail[0]
    else: email = None

    newContact = Contact(firstName, phone, middleName, lastName, email)
    phonebookHash.insert(newContact)
    utils.clearScreen()
    print("Contact was added successfully")
    utils.goBack()

    """
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
"""
def view_contacts():
    utils.clearScreen()
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

#def test():
    
