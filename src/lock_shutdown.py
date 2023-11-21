"""
    Choose to lock or shutdown Windows.
    This one is actually more difficult to use than just doing a
    keybind.
"""
import ctypes
import os

usr_input = input("1 to lock, 2 to shutdown ")

# Using strings because I can't be assed setting up safety for an int input
if usr_input == "1":
    ctypes.windll.user32.LockWorkStation()
elif usr_input == "2":
    choice = input("You sure? Y/N ").lower().strip()
    if choice == "y":
        os.system("shutdown /s /t 0")
    else:
        print("ITS NOT,")
        print("ITS NOT SHUTTING DOWN!")
        print("UWOOOOOOOOOOOOOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!")
