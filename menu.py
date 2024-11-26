import utils
from visualizer import visualize
from contact import Contact
from hash import HashTable

phonebookHash = HashTable()
phonebookHash.load()

def addContact():

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
    phonebookHash.save()
    visualize(phonebookHash)


def viewContacts():
    utils.clearScreen()
    phonebookHash.display()
    utils.goBack()

def searchContact():
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

def updateContact():
    utils.clearScreen()
    print("This is an updateContact function")
    utils.goBack()

def deleteContact():
    global phonebookHash  # Tell Python to use the global variable
    utils.clearScreen()
    name = input("Enter a name to delete a contact\n(\'Delete All\' to delete all contacts): ").strip().lower().split() or None
    fullName = " ".join(name) if name else None
    if fullName.lower() == "delete all": 
        newPhonebookHash = HashTable()
        phonebookHash = newPhonebookHash
        phonebookHash.save()
        print("The Phonebook has been erased successfully")
        utils.goBack()
        return
    fullName = " ".join(name) if name else None
    result = phonebookHash.searchContacts(fullName)
    if result:
        if len(result) == 1:
            verifyDeleteContact(result[0].fullName)
            return           
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
                        verifyDeleteContact(result[option - 1].fullName)
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
    else:
        print("No matching contacts found.")
        utils.goBack()

def verifyDeleteContact(name):
    utils.clearScreen()
    while True:
        question = input(f"Do you want to delete the contact \'{name}\'  (Y / N) ? :")
        if question.lower() == "y":
            phonebookHash.deleteOneContact(name)
            phonebookHash.save()
            visualize(phonebookHash)
            return
        elif question.lower() == "n": return
        else: 
            print("Invalid input! Try again\n")