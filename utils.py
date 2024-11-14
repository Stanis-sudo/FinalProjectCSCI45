import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def go_back():
    user_input = input("<--Back  ")
    if user_input.lower() == "back" or user_input == "":
        return True
    else:
        return False
    time.sleep(1/100)