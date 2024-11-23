

import utils
import pickle
from icecream import ic

class HashTable:

    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.maxElements = 0

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
        self.maxElements = max(len(bucket) for bucket in self.table) if self.table else 0
        if self.maxElements > 2:
            self.resize()
            ic(f"Hash Size: {len(self.table)}")
            utils.goBack()
            return
        

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:")
            for contact in bucket:
                print(contact)
            print()

    def resize(self):
        newHashTable = HashTable(len(self.table) * 2)
        for i, bucket in enumerate(self.table):
            for contact in bucket:
                newHashTable.insert(contact)
        self.table = newHashTable.table

    def save(self, filename ='hashData.pkl'):
        data = []
        for bucket in self.table:
            data.extend(bucket)
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print(" Data Saved.")

    def load (self,filename = 'hashData.pkl'):
        try:
            with open(filename, 'rb') as file:
                if file.readable() and file.peek(1):
                    data = pickle.load(file)
                    print("Data Loaded.")
                    self.table = [[] for _ in range(self.size)]
                    for value in data:
                        self.insert(value)
                else:
                    print("Empty file")
                    self.table = [[] for _ in range(self.size)]
        except FileNotFoundError:
            print("No Data Found.")
            self.table = [[] for _ in range(self.size)]
        except Exception as e:
            print(f"Error loading file: {e}")


