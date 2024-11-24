import utils

import visualizer
from contact import Contact
from hash import HashTable

phonebook = {}
phonebookHash = HashTable()
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
    visualizer.visualize(phonebookHash)
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

def search_contact():
    utils.clearScreen()
    name = input("Enter a name to search: ").strip().lower().split() or None
    fullName = " ".join(name) if name else None
    result = phonebookHash.searchContacts(fullName)
    if result:
        if len(result) == 1:
            utils.clearScreen()
            print(result[0])
        else:
            for i, contact in enumerate(result):
                print(f"{i + 1}: {contact.fullName}")
            while True:
                try:
                    userInput = input("\nChoose the option or press Enter to return: ")
                    if userInput == "": return
                    option = int(userInput)         # Convert input to an integer
                    if option < 1 or option > len(result):
                        print("Invalid input! Please enter a valid number.")
                    else :
                        utils.clearScreen()
                        print(result[option - 1])
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

    else:
        print("No matching contacts found.")
    utils.goBack()
        

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
    
