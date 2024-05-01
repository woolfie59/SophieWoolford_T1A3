def plant_crop():
    print("What would you like to do?")
    print("Plant a turnip --> turnip")
    print("Plant a carrot --> carrot")
    print("Plant a potato --> potato")
    print("Back to main menu --> exit")

    crop_choice = input("Enter your selection: ")
    return crop_choice

crop_choice = ""

while not crop_choice.startswith("exit"):
    crop_choice = plant_crop()

    if (crop_choice == "turnip"):
        print("You planted a turnip!")
    elif (crop_choice == "carrot"):
        print("You planted a carrot!")
    elif (crop_choice == "potato"):
        print("You planted a potato!")
    elif (crop_choice == "exit"):
        print("Exiting to the main menu")
    else:
        print("You goofball! Select turnip or carrot or potato or exit from the menu.")




def harvest_crop():
    print("What would you like to do?")
    print("Harvest a turnip --> turnip")
    print("Harvest a carrot --> carrot")
    print("Harvest a potato --> potato")
    print("Back to main menu --> exit")

    harvest_choice = input("Enter your selection: ")
    return harvest_choice

harvest_choice = ""


def view_crops():
    print("Here are your vegetables!")