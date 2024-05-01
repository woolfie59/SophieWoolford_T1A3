def plant_crop():
    print("What seed would you like to plant?")
    print("Turnip")
    print("Carrot")
    print("Potato")
    print("Exit to main menu")

    crop_choice = input("Enter your selection: ")
    return crop_choice

crop_choice = ""

while not crop_choice.startswith("Exit"):
    crop_choice = plant_crop()

    if (crop_choice == "Turnip"):
        print("You planted a turnip!")
    elif (crop_choice == "Carrot"):
        print("You planted a carrot!")
    elif (crop_choice == "Potato"):
        print("You planted a potato!")
    elif (crop_choice == "Exit"):
        print("Exiting to the main menu")
    else:
        print("You goofball! Select Turnip or Carrot or Potato or Exit from the menu.")




def harvest_crop():
    print("Harvest a crop")

def view_crops():
    print("View crops")