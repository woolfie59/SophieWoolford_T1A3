def plant_crop():
    crop_choice = get_crop_choice()
    while not crop_choice.startswith("e"):
        if (crop_choice == "b"):
            print("\n   You planted a \033[1mbroccoli!\033[0m")
        elif (crop_choice == "c"):
            print("\n   You planted a \033[1mcarrot!\033[0m")
        elif (crop_choice == "p"):
            print("\n   You planted a \033[1mpotato!\033[0m")
        elif (crop_choice == "e"):
            print("   Exiting to the main menu")
            return
        else:
            print("\n   \033[91m\033[1mYou goofball! Enter b or c or p or e in the menu.\033[0m\n")

        crop_choice = get_crop_choice()

def get_crop_choice():
    print("\nWhat would you like to do?\n")
    print("   To plant a \033[1mbroccoli\033[0m, enter: \033[1mb\033[0m")
    print("   To plant a \033[1mcarrot\033[0m, enter: \033[1mc\033[0m")
    print("   To plant a \033[1mpotato\033[0m, enter: \033[1mp\033[0m")
    print("   To \033[1mexit\033[0m to main menu, enter: \033[1me\033[0m")

    return input("\nEnter you selection: ")

import csv

def read_vegetable_counts_from_csv(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            counts = {row[0]: int(row[1]) for row in reader}
    except FileNotFoundError:
        counts = {'broccoli': 0, 'carrot': 0, 'potato': 0}
    return counts

def write_vegetable_counts_to_csv(file_name, counts):
    with open(file_name, 'w', newline='') as file:
        writer =csv.writer(file)
        for vegetable, count in counts.items():
            writer.writerow([vegetable, count])

def display_csv_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]}: {row[1]}")
    except FileNotFoundError:
        print("\n   \033[91m\033[1mYou goofball! Plant and harvest vegetables to view them here.\033[0m")

def harvest_crop():
    csv_file_name = "vegetable_counts.csv"
    vegetable_counts = read_vegetable_counts_from_csv(csv_file_name)

    harvest_choice = get_harvest_choice()
    while not harvest_choice.startswith("e"):
        print(harvest_choice)

        if (harvest_choice == "b"):
            print("   You harvested a \033[1mbroccoli!\033[0m \U0001F966")
            vegetable_counts['broccoli'] += 1
        elif (harvest_choice == "c"):
            print("   You harvested a \033[1mcarrot!\033[0m \U0001F955")
            vegetable_counts['carrot'] += 1
        elif (harvest_choice == "p"):
            print("   You harvested a \033[1mpotato!\033[0m \U0001F954")
            vegetable_counts['potato'] += 1
        elif (harvest_choice == "e"):
            print("   Exiting to the main menu")
            write_vegetable_counts_to_csv(csv_file_name, vegetable_counts)
            return
        else:
            print("\n   \033[91m\033[1mYou goofball! Enter b or c or p or e in the menu.\033[0m\n")

        harvest_choice = get_harvest_choice()

    write_vegetable_counts_to_csv(csv_file_name, vegetable_counts)

def get_harvest_choice():
    print("\nWhat would you like to do?\n")
    print("To harvest a \033[1mbroccoli\033[0m, enter: \033[1mb\033[0m")
    print("To harvest a \033[1mcarrot\033[0m, enter: \033[1mc\033[0m")
    print("To harvest a \033[1mpotato\033[0m, enter: \033[1mp\033[0m")
    print("To \033[1mexit\033[0m to main menu, enter: \033[1me\033[0m")

    return input("\nEnter you selection: ")

def view_crops():
    print("\n\033[1mHere are your vegetables!\033[0m")
    csv_file_name = "vegetable_counts.csv"
    display_csv_contents(csv_file_name)