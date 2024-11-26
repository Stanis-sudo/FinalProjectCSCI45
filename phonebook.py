import utils
import menu
import time

def main():
    while True:
        
        utils.clearScreen()
        print("\n.:: Phonebook Menu ::.\n")
        print(" 1. Add Contact")
        print(" 2. View Contacts")
        print(" 3. Search Contact")
        print(" 4. Update Contact")
        print(" 5. Delete Contact")
        print(" 6. Exit")
        if menu.phonebookHash.contactCount > 0:
            print(f"\n Total records: {menu.phonebookHash.contactCount}\n")
        else:
            print("\n Phonebook is empty")
        choice = input(" Choose an option: ")
        if choice == "1":
            menu.addContact()
        elif choice == "2":
            menu.viewContacts()
        elif choice == "3":
            menu.searchContact()
        elif choice == "4":
            menu.updateContact()
        elif choice == "5":
            menu.deleteContact()
        elif choice == "6" or choice.lower() == "exit":
            utils.clearScreen()
            print("Exiting phonebook. Goodbye!")
            break
        else:
            print("\n Invalid option, please try again.")
        time.sleep(1/100)

if __name__ == "__main__":
    main()
