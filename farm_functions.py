def plant_crop():
    crop_choice = get_crop_choice()
    while not crop_choice.startswith("e"):
        print(crop_choice)

        if (crop_choice == "b"):
            print("   You planted a broccoli!")
        elif (crop_choice == "c"):
            print("   You planted a carrot!")
        elif (crop_choice == "p"):
            print("   You planted a potato!")
        elif (crop_choice == "e"):
            print("   Exiting to the main menu")
            return
        else:
            print("\nYou goofball! Enter b or c or p or e in the menu.\n")

        crop_choice = get_crop_choice()

def get_crop_choice():
    print("\nWhat would you like to do?\n")
    print("   To plant a broccoli, enter: b")
    print("   To plant a carrot, enter: c")
    print("   To plant a potato, enter: p")
    print("   To exit to main menu, enter: e")

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
        print("\nYou goofball! Plant and harvest vegetables to view them here.")

def harvest_crop():
    csv_file_name = "vegetable_counts.csv"
    vegetable_counts = read_vegetable_counts_from_csv(csv_file_name)

    harvest_choice = get_harvest_choice()
    while not harvest_choice.startswith("e"):
        print(harvest_choice)

        if (harvest_choice == "b"):
            print("   You harvested a broccoli! \U0001F966")
            vegetable_counts['broccoli'] += 1
        elif (harvest_choice == "c"):
            print("   You harvested a carrot! \U0001F955")
            vegetable_counts['carrot'] += 1
        elif (harvest_choice == "p"):
            print("   You harvested a potato! \U0001F954")
            vegetable_counts['potato'] += 1
        elif (harvest_choice == "e"):
            print("   Exiting to the main menu")
            write_vegetable_counts_to_csv(csv_file_name, vegetable_counts)
            return
        else:
            print("\nYou goofball! Enter b or c or p or e in the menu.\n")

        harvest_choice = get_harvest_choice()

    write_vegetable_counts_to_csv(csv_file_name, vegetable_counts)

def get_harvest_choice():
    print("\nWhat would you like to do?\n")
    print("To harvest a broccoli, enter: b")
    print("To harvest a carrot, enter: c")
    print("To harvest a potato, enter: p")
    print("To exit to main menu, enter: e")

    return input("\nEnter you selection: ")

def view_crops():
    print("\nHere are your vegetables!")
    csv_file_name = "vegetable_counts.csv"
    display_csv_contents(csv_file_name)