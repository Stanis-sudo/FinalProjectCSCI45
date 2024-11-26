import utils
import menu
import time

def main():
    menu.init()
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
        choice = input(" Choose an option: ").strip()
        if menu.menuSelector(choice):
            return
        time.sleep(1/200)

if __name__ == "__main__":
    main()
