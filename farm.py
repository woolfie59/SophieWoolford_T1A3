
# System packages
import os.path, csv

# External packages

# Imports of own functions
from farm_functions import plant_crop, harvest_crop, view_crops

print("\n\033[1mWelcome to your farm! \U0001F920 \U0001F331\033[0m")

def farm_menu():
    print("\nTo \033[1mplant\033[0m a crop, enter \033[1m1\033[0m.")
    print("To \033[1mharvest\033[0m a crop, enter \033[1m2\033[0m.")
    print("To \033[1mview\033[0m your crops, enter \033[1m3\033[0m.")
    print("To \033[1mleave\033[0m your farm, enter \033[1m4\033[0m.")

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
        print("\n   \033[91m\033[1mYou goofball! Select 1 or 2 or 3 or 4 from the menu.\033[0m")

print("See ya later, farmer! \U0001F920")
