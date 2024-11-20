import os
import time

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def goBack():
    user_input = input("<--Back  ")
    if user_input.lower() == "back" or user_input == "":
        return True
    else:
        return False