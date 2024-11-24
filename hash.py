
import math
import utils
import pickle
import time
from visualizer import visualize
from icecream import ic

fileName = 'hashData.pkl'
maxCountBucket = 5
hashInitSize = 3

class HashTable:

    def __init__(self, size = hashInitSize):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.maxElements = 0
        self.contactCount = 0

    def customHash(self, key):
        #hashValue = sum(ord(char) for char in key)

        hashValue = 5381  # A common initial value for DJB2
        for char in key:
            hashValue = (hashValue * 33) + ord(char)  # Hashing with multiplication by 33
        return hashValue % self.size
    
    def customPoliHash(self, key):
        base = 31
        mod = self.size
        hashValue = 0
        power = 1  # Represents base^i % mod
        
        for char in key:
            hashValue = (hashValue + ord(char) * power) % mod
            power = (power * base) % mod  # Update power for the next character
        
        return hashValue
    
    def insert(self, contact):
        index = self.customPoliHash(contact.fullName)
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
        self.contactCount += 1
        self.maxElements = max(len(bucket) for bucket in self.table) if self.table else 0
        if self.maxElements > maxCountBucket:
            #ic(self.table)
            self.resize()
            #ic(f"Hash Size: {len(self.table)}")
            #utils.goBack()
            return
        

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:")
            for contact in bucket:
                print(contact)
            print()

    def resize(self):
        newHashTable = HashTable(math.ceil(len(self.table) / 0.7))
        for i, bucket in enumerate(self.table):
            for contact in bucket:
                newHashTable.insert(contact)
        self.table = newHashTable.table

    def save(self, filename = fileName):
        data = []
        for bucket in self.table:
            data.extend(bucket)
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print(" Data Saved.")

    def load (self,filename = fileName):
        try:
            with open(filename, 'rb') as file:
                if file.readable() and file.peek(1):
                    data = pickle.load(file)
                    print("Data Loaded.")
                    # Calculate the minimum size based on the load factor
                    minSize = math.ceil(len(data) / 0.7)
                    # Round up to the next power of 2 for better performance
                    #newSize = 2**math.ceil(math.log2(min_size))
                    #ic(self.size, len(data), newSize)

                    # Find next prime number
                    while not self.isPrime(minSize):
                        minSize += 1
                    self.table = [[] for _ in range(minSize)]
                    self.size = minSize
                    ic(len(self.table))
                    utils.goBack()
                    count = 0
                    for value in data:
                        self.insert(value)
                        #ic(self.table)
                        #utils.goBack()
                        visualize(self)
                        count += 1
                        ic("Visualize # ", count)
                        #time.sleep(0.5)
                else:
                    print("Empty file")
                    self.table = [[] for _ in range(self.size)]
        except FileNotFoundError:
            print("No Data Found.")
            self.table = [[] for _ in range(self.size)]
        except Exception as e:
            print(f"Error loading file: {e}")

    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True