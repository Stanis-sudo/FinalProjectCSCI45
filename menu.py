import utils
import datetime
import time
from visualizer import visualize
from contact import Contact
from hash import HashTable
from icecream import ic

ic.disable()

phonebookHash = HashTable()

def init():
    with open("visualizer.log", "a") as file:
        print("<-----New session----->\n", file = file)
    utils.clearScreen()
    print(" ___ _  _  ___  _  _ ___ ___  ___   ___  _  __")
    print("| _ \ || |/ _ \| \| | __| _ )/ _ \ / _ \| |/ /")
    print("|  _/ __ | (_) | .` | _|| _ \ (_) | (_) | ' < ")
    print("|_| |_||_|\___/|_|\_|___|___/\___/ \___/|_|\_\\")
    print("\n\nInitialization...")
    startTime = datetime.datetime.now()
    phonebookHash.load()
    remTime = datetime.datetime.now() - startTime - datetime.timedelta(seconds = 1.5)
    # Check if the remaining time is less than 0
    if remTime.total_seconds() < 0:
        time.sleep(abs(remTime.total_seconds()))

def menuSelector(choice):
    if choice in ["1", "2", "3", "4", "5", "6"]:
        utils.clearScreen()
        if choice == "1":
            addContact()
        elif choice == "2":
            viewContacts()
        elif choice == "3":
            if searchContact() == False: return
        elif choice == "4":
            ic("Update contact")
            updateContact()
        elif choice == "5":
            deleteContact()
        elif choice == "6" or choice.lower() == "exit":
            utils.clearScreen()
            print("Exiting phonebook. Goodbye!")
            return True
    else:
        print("\n Invalid option, please try again.")
    utils.goBack()
    return False

def getInput(message, isRequired, inputName = None):
    while True:
        userInput = input(message).strip().title().split() or None
        if userInput is not None:
            validInput = userInput[0]
            return validInput
        elif isRequired:
            #utils.clearScreen()
            print(f"Error!\n{inputName} cannot be empty")
            continue
        else: return None


def addContact():
    #Get a new Contact data
    firstName = getInput("First Name:                                 ", True, "First Name")
    middleName = getInput("Middle Name (To skip press Enter):          ", False)
    lastName = getInput("Last Name (To skip press Enter):            ", False)
    phone = getInput("Phone Number:                               ", True, "Phone Number")
    email = getInput("Email Address (To skip press Enter):        ", False)
    #Save the new Contact
    newContact = Contact(firstName, phone, middleName, lastName, email)
    phonebookHash.insert(newContact)
    phonebookHash.save()
    visualize(phonebookHash, "menu.addContact function")
    utils.clearScreen()
    print("Contact was added successfully")


def viewContacts():
    phonebookHash.display()

def searchContact():
    utils.clearScreen()
    name = input("Enter a name to search: ").strip().lower().split() or None
    if not name: return False
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
                    if userInput == "": return False
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
    return True

def updateContact():
    name = input("Enter a name to update a contact: ").strip().lower().split() or None
    if not name: return
    updateName = searchForName(name)
    if updateName:
        print("Needs to be implemented")
        print(" 1. Update First Name")
        print(" 2. Update Middle Name")
        print(" 3. Update Last Name")
        print(" 4. Update Phone Number")
        print(" 5. Update Email Address")
        choice = input(" Choose an option: ").strip()
        updateSelector(choice, updateName)

def updateSelector(choice, fullName):
    while True:
        if choice in ["1", "2", "3", "4", "5"]:
            utils.clearScreen()
            if choice == "1":
                firstName = getInput("First Name:                                 ", True, "First Name")
                for bucket in phonebookHash.table:
                    for contact in bucket:
                        if fullName in contact.fullName:
                            newFullName = " ".join(filter(None, [firstName, contact.middleName, contact.lastName]))
                            contact.inputPhone = phone
                            print(f"Phone Number for {fullName} was updated")

                break
            elif choice == "2":
                viewContacts()
                break
            elif choice == "3":
                if searchContact() == False: return
                break
            elif choice == "4":
                phone = getInput("Phone Number:                               ", True, "Phone Number")
                updateInfo(fullName, "Phone Number", phone)
                break
            elif choice == "5":
                email = getInput("Email Address (To skip press Enter):        ", False)
                updateInfo(fullName, "Email Address", email)
                break
        else:
            print("\n Invalid option, please try again.")

def updateInfo(fullName, param, newValue):
    for bucket in phonebookHash.table:
        for contact in bucket:
            if fullName in contact.fullName:
                if param == "Phone Number":
                    contact.phoneNumber = newValue
                elif param == "Email Address":
                    contact.emailAddress = newValue
    print(f"{param} for {fullName} was updated")

def deleteContact():
    global phonebookHash  # Tell Python to use the global variable
    name = input("Enter a name to delete a contact\n(\'Delete All\' to delete all contacts): ").strip().lower().split() or None
    if not name: return
    fullName = " ".join(name) if name else None
    if fullName.lower() == "delete all": 
        newPhonebookHash = HashTable()
        phonebookHash = newPhonebookHash
        phonebookHash.save()
        print("The Phonebook has been erased successfully")
        return
    deleteName = searchForName(name)
    if deleteName:
        verifyDeleteContact(deleteName)
    
def searchForName(name):
    fullName = " ".join(name) if name else None
    if not fullName: return None
    result = phonebookHash.searchContacts(fullName)
    if result:
        if len(result) == 1:
            return result[0].fullName
        else:
            for i, contact in enumerate(result):
                print(f"{i + 1}: {contact.fullName}")
            while True:
                try:
                    userInput = input("\nChoose the option or press Enter to return: ")
                    if userInput == "": return None
                    option = int(userInput)         # Convert input to an integer
                    if option < 1 or option > len(result):
                        print("Invalid input! Please enter a valid number.")
                    else :
                        return result[option - 1].fullName
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
    else:
        print("No matching contacts found.")
        return None

def verifyDeleteContact(fullName):
    while True:
        question = input(f"Do you want to delete the contact \'{fullName}\'  (Y / N) ? :")
        if question.lower() == "y":
            phonebookHash.deleteOneContact(fullName)
            phonebookHash.save()
            visualize(phonebookHash, "menu.verifyDeleteContact function")
            return
        elif question.lower() == "n": return
        else: 
            print("Invalid input! Try again\n")