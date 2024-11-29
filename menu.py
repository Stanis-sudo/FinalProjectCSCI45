import utils
import datetime
import time
import re
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

def getInput(message, inputName = None):
    while True:
        if inputName in ["First Name", "Middle Name", "Last Name"]:
            userInput = input(message).strip().title().split() or None
        elif inputName == "Phone Number":
            userInput = input(message).strip() or None
        else:
            userInput = input(message).strip().lower().split() or None
        if userInput is not None:
            if inputName != "Phone Number":
                validInput = userInput[0]
            else:
                validInput = userInput
            return validInput
        elif inputName in ["First Name", "Phone Number"]:
            #utils.clearScreen()
            print(f"Error!\n{inputName} cannot be empty")
            continue
        else: return None

def isValidNumber(phone):
    pattern = re.compile(r'^(\+?\d{1,3})?[-.\s]?(\(?\d{3}\)?)[-.\s]?\d{3}[-.\s]?\d{4}$')
    if not bool(pattern.match(phone)):
        return None
    
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    # Check if the phone number has exactly 10 digits
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        return None  # Return None for invalid phone numbers

def addContact():
    #Get a new Contact data
    firstName = getInput("First Name:                                 ", "First Name")
    middleName = getInput("Middle Name (To skip press Enter):          ", "Middle Name")
    lastName = getInput("Last Name (To skip press Enter):            ", "Last Name")
    while True:
        userPhone = getInput("Phone Number (10 digits):                   ", "Phone Number")
        phone = isValidNumber(userPhone)
        if phone:
            break
        else: print(f"{userPhone} is not a valid Phone Number")
    email = getInput("Email Address (To skip press Enter):        ")
    #Save the new Contact
    newContact = Contact(firstName, phone, middleName, lastName, email)
    phonebookHash.insert(newContact)
    phonebookHash.save()
    visualize(phonebookHash, "menu.addContact function")
    utils.clearScreen()
    print("Contact was added successfully")

def viewContacts():
    if phonebookHash.isEmpty(): return
    phonebookHash.display()

def searchContact():
    utils.clearScreen()
    if phonebookHash.isEmpty(): return True
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
    if phonebookHash.isEmpty(): return
    name = input("Enter a name to update a contact: ").strip().lower().split() or None
    if not name: return
    updateName = searchForName(name)
    if updateName:
        while True:
            print(f"Updating contact {updateName}\n")
            print(" 1. Update First Name")
            print(" 2. Update Middle Name")
            print(" 3. Update Last Name")
            print(" 4. Update Phone Number")
            print(" 5. Update Email Address")
            print(" 6. Cancel")
            choice = input("\n Choose an option: ").strip() or None
            if not choice: return
            if updateSelector(choice, updateName): return

def updateSelector(choice, fullName):
        if choice in ["1", "2", "3", "4", "5", "6"]:
            utils.clearScreen()
            if choice == "1":
                firstName = getInput("First Name:                                 ", True, "First Name")
                updateInfo(fullName, "First Name", firstName)
                return True
            elif choice == "2":
                middleName = getInput("Middle Name:                                 ", False)
                updateInfo(fullName, "Middle Name", middleName)
                return True
            elif choice == "3":
                lastName = getInput("Last Name:                                 ", False)
                updateInfo(fullName, "Last Name", lastName)
                return True
            elif choice == "4":
                phone = getInput("Phone Number:                               ", True, "Phone Number")
                updateInfo(fullName, "Phone Number", phone)
                return True
            elif choice == "5":
                email = getInput("Email Address (To skip press Enter):        ", False)
                updateInfo(fullName, "Email Address", email)
                return True
            elif choice == "6":
                return True
        else:
            print("\n Invalid option, please try again.")
            return False

def updateInfo(fullName, param, newValue):
    updated = False
    for bucket in phonebookHash.table:
        for contact in bucket:
            if fullName in contact.fullName:
                if param == "Phone Number":
                    contact.phoneNumber = newValue
                    updated = True
                    break  # Breaks out of the inner loop
                elif param == "Email Address":
                    contact.emailAddress = newValue
                    updated = True
                    break  # Breaks out of the inner loop
                else: 
                    updateName(contact, fullName, param, newValue)
                    ic("inside updateName")
                    updated = True
                    break  # Breaks out of the inner loop
        if updated:
            phonebookHash.save()
            print(f"{param} for {fullName} was updated")
            break  # Breaks out of the outer loop

def updateName(contact, fullName, param, newValue):
    if param == "First Name":
        newFullName = " ".join(filter(None, [newValue, contact.middleName, contact.lastName]))
        ic(fullName)
        ic(newFullName)
        newContact = Contact(newValue, contact.phoneNumber, contact.middleName, contact.lastName, contact.emailAddress)
    elif param == "Middle Name":
        newFullName = " ".join(filter(None, [contact.firstName, newValue, contact.lastName]))
        newContact = Contact(contact.firstName, contact.phoneNumber, newValue, contact.lastName, contact.emailAddress)
    elif param == "Last Name":
        newFullName = " ".join(filter(None, [contact.firstName, contact.middleName, newValue]))
        newContact = Contact(contact.firstName, contact.phoneNumber, contact.middleName, newValue, contact.emailAddress)
        ic(newContact)
    if doesExist(newFullName):
        print(f"Contact {newFullName} already exists in the Phonebook")
        return
    else:
        ic("Creating a new Contact for Update function")
        phonebookHash.deleteOneContact(fullName)
        phonebookHash.insert(newContact)
        visualize(phonebookHash, "menu.updateInfo.firstName function")

def doesExist(fullName):
    ic("doesExist func: ", fullName)
    for bucket in phonebookHash.table:
        for contact in bucket:
            if fullName == contact.fullName:
                ic("return true for doesExist")
                return True
    ic("return false for doesExist")
    return False

def deleteContact():
    global phonebookHash  # Tell Python to use the global variable
    if phonebookHash.isEmpty(): return
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