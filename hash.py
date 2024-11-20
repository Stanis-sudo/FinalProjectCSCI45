import utils

class HashTable:

    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def customHash(self, key):
        hashValue = sum(ord(char) for char in key)
        return hashValue % self.size
    
    def insert(self, contact):
        index = self.customHash(contact.fullName)
        bucket = self.table[index]

        for i, contactExist in enumerate(bucket):
            if contactExist.fullName == contact.fullName:
                while True:
                    utils.clearScreen
                    yesNo = input(f"The contact {contact.fullName} already exist in the Phonebook.\n Do you want to update the existing contact?\nY/N")
                    if yesNo == "Y":
                        bucket[i] = contact
                        return
                    elif yesNo == "N":
                        return
                    else: 
                        print("Wrong input. Try again")
                        continue
            
        bucket.append(contact)

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:")
            for contact in bucket:
                print(contact)
            print()