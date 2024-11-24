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
        print(" 4. Delete Contact")
        print(" 5. Save and Exit")
        if menu.phonebookHash.contactCount > 0:
            print(f"\n Total records: {menu.phonebookHash.contactCount}\n")
        else:
            print(" Phonebook is empty")
        choice = input(" Choose an option: ")
        if choice == "1":
            menu.add_contact()
        elif choice == "2":
            menu.view_contacts()
        elif choice == "3":
            menu.search_contact()
        elif choice == "4":
            menu.delete_contact()
        elif choice == "5" or choice.lower() == "exit":
            utils.clearScreen()
            menu.phonebookHash.save()
            print("Exiting phonebook. Goodbye!")
            break
        else:
            print("\n Invalid option, please try again.")
        time.sleep(1/100)

if __name__ == "__main__":
    main()
