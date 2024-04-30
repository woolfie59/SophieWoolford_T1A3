
# System packages
import os.path

# External packages

# Imports of our own functions
from farm_functions import plant_crop, harvest_crop, view_crops

print("Welcome to your farm!")

def farm_menu():
    print("Enter 1 to plant a crop.")
    print("Enter 2 to harvest a crop.")
    print("Enter 3 to view your crops.")
    print("Enter 4 to leave your farm.")

    user_choice = input("Enter your selection: ")
    return user_choice

file_name = "list.csv"

if (not os.path.isfile(file_name)):
    farm_file = open(file_name, "w")
    farm_file.write("crop,amount\n")
    farm_file.close()

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
        print("You entered 4.")
    else:
        print("You goofball! Select 1 or 2 or 3 or 4 from the menu.")

print("See ya later, farmer!")

# Entered 1 in main menu
# def plant_crop():
#     crop_choice = ""

# while crop_choice != "4":
#     crop_choice = plant_crop()

#     if (crop_choice == "Turnip"):
#         print("You planted a turnip!")
#     elif (crop_choice == "Carrot"):
#         print("You planted a carrot!")
#     elif (crop_choice == "Potato"):
#         print("You planted a potato!")
#     elif (crop_choice == "Exit"):
#         print("Exiting to the main menu")
#         farm_menu()
#     else:
#         print("You goofball! Select Turnip or Carrot or Potato or Exit from the menu.")
    


