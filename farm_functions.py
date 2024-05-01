def plant_crop():
    crop_choice = get_crop_choice()
    while not crop_choice.startswith("exit"):
        print(crop_choice)

        if (crop_choice == "turnip"):
            print("You planted a turnip!")
        elif (crop_choice == "carrot"):
            print("You planted a carrot!")
        elif (crop_choice == "potato"):
            print("You planted a potato!")
        elif (crop_choice == "exit"):
            print("Exiting to the main menu")
            return
        else:
            print("You goofball! Select turnip or carrot or potato or exit from the menu.")

        crop_choice = get_crop_choice()

def get_crop_choice():
    print("What seed would you like to plant?")
    print("Turnip")
    print("Carrot")
    print("Potato")
    print("Exit to main menu")

    return input("Enter you selection: ")


def harvest_crop():
    harvest_choice = get_harvest_choice()
    while not harvest_choice.startswith("exit"):
        print(harvest_choice)

        if (harvest_choice == "turnip"):
            print("You harvested a turnip!")
        elif (harvest_choice == "carrot"):
            print("You harvested a carrot!")
        elif (harvest_choice == "potato"):
            print("You harvested a potato!")
        elif (harvest_choice == "exit"):
            print("Exiting to the main menu")
            return
        else:
            print("You goofball! Select turnip or carrot or potato or exit from the menu.")

        harvest_choice = get_harvest_choice()

def get_harvest_choice():
    print("What crop would you like to harvest?")
    print("Turnip")
    print("Carrot")
    print("Potato")
    print("Exit to main menu")

    return input("Enter you selection: ")


def view_crops():
    print("Here are your vegetables!")