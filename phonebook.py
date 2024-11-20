import utils
import menu
import time

def main():
    while True:
        utils.clear_screen()
        print("\n.:: Phonebook Menu ::.\n")
        print(" 1. Add Contact")
        print(" 2. View Contacts")
        print(" 3. Search Contact")
        print(" 4. Delete Contact")
        print(" 5. Exit")
        choice = input("\n Choose an option: ")
        if choice == "1":
            menu.add_contact()
        elif choice == "2":
            menu.view_contacts()
        elif choice == "3":
            menu.search_contact()
        elif choice == "4":
            menu.delete_contact()
        elif choice == "5" or choice.lower() == "exit":
            utils.clear_screen()
            print("Exiting phonebook. Goodbye!")
            break
        elif choice == "6":
            menu.test()
        else:
            print("\n Invalid option, please try again.")
        time.sleep(1/100)

main()