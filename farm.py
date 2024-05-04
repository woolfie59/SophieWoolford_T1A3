
# System packages
import os.path, csv

# External packages

# Imports of own functions
from farm_functions import plant_crop, harvest_crop, view_crops

print("Welcome to your farm! \U0001F920 \U0001F331")

def farm_menu():
    print("\nEnter 1 to plant a crop.")
    print("Enter 2 to harvest a crop.")
    print("Enter 3 to view your crops.")
    print("Enter 4 to leave your farm.")

    user_choice = input("\nPlease enter your selection: ")
    return user_choice

crop_yield = "list.csv"

if (not os.path.isfile(crop_yield)):
    crop_yield = open(crop_yield, "w")
    crop_yield.write("crop,amount\n")
    crop_yield.close()

choice = ""

while choice != "4":
    choice = farm_menu()

    if (choice == "1"):
        plant_crop()
    elif (choice == "2"):
        harvest_crop()
    elif (choice == "3"):
        view_crops()
    elif (choice == "4"):
        print("\nYou're leaving.")
    else:
        print("\nYou goofball! Select 1 or 2 or 3 or 4 from the menu.")

print("See ya later, farmer!")
