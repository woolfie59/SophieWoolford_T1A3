from rich import print
from rich.console import Console

console = Console()

# Main menu selection 1 -> sub-menu plant menu, def with while loop
def plant_crop():
    crop_choice = get_crop_choice()
    while not crop_choice.startswith("e"):
        crop_choice = crop_choice.lower() # Converts input to lowercase, user can use upper- or lowercase
        if (crop_choice == "b"):
            print("\n   You planted a [bold]broccoli![/bold]")
        elif (crop_choice == "c"):
            print("\n   You planted a [bold]carrot![/bold]")
        elif (crop_choice == "p"):
            print("\n   You planted a [bold]potato![/bold]")
        elif (crop_choice == "e"):
            print("   Exiting to the main menu")
            return
        else:
            print("\n   [bold red]You goofball! Enter B or C or P or E in the menu.[/bold red]")

        crop_choice = get_crop_choice()

# Selectors for plant menu
def get_crop_choice():
    print("\nWhat would you like to do?\n")
    print("   To plant a [bold]broccoli[/bold], enter: [bold]B[/bold]")
    print("   To plant a [bold]carrot[/bold], enter: [bold]C[/bold]")
    print("   To plant a [bold]potato[/bold], enter: [bold]P[/bold]")
    print("   To [bold]exit[/bold] to main menu, enter: [bold]E[/bold]")

    return input("\nEnter you selection: ")

# Creation of csv file for harvest count
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
        print("\n   [bold red]You goofball! Plant and harvest vegetables to view them here.[/bold red]")

# Main menu selection 2 -> sub-menu harvest menu, def with while loop
# Reads user input and adds to csv file to keep count of amount of harvested vegetables
def harvest_crop():
    csv_file_name = "vegetable_counts.csv"
    vegetable_counts = read_vegetable_counts_from_csv(csv_file_name)

    harvest_choice = get_harvest_choice()
    while not harvest_choice.startswith("e"):
        harvest_choice = harvest_choice.lower() # Converts input to lowercase, user can use upper- or lowercase
        if (harvest_choice == "b"):
            print("\n   You harvested a [bold]broccoli![/bold]", ":broccoli:")
            vegetable_counts['broccoli'] += 1
        elif (harvest_choice == "c"):
            print("\n   You harvested a [bold]carrot![/bold]", ":carrot:")
            vegetable_counts['carrot'] += 1
        elif (harvest_choice == "p"):
            print("\n   You harvested a [bold]potato![/bold]", ":potato:")
            vegetable_counts['potato'] += 1
        elif (harvest_choice == "e"):
            print("\n   Exiting to the main menu")
            write_vegetable_counts_to_csv(csv_file_name, vegetable_counts)
            return
        else:
            print("\n   [bold red]You goofball! Enter b or c or p or e in the menu.[/bold red]\n")

        harvest_choice = get_harvest_choice()

    write_vegetable_counts_to_csv(csv_file_name, vegetable_counts)

# Harvest menu printed to user
def get_harvest_choice():
    print("\nWhat would you like to do?\n")
    print("To harvest a [bold]broccoli[/bold], enter: [bold]B[/bold]")
    print("To harvest a [bold]carrot[/bold], enter: [bold]C[/bold]")
    print("To harvest a [bold]potato[/bold]m, enter: [bold]P[/bold]")
    print("To [bold]exit[/bold] to main menu, enter: [bold]E[/bold]")

    return input("\nEnter you selection: ")

# Main menu selection 2 -> view crops, through csv file handling
def view_crops():
    print("\n[bold]Here are your vegetables![/bold]", ":broccoli:", ":carrot:", ":potato:")
    csv_file_name = "vegetable_counts.csv"
    display_csv_contents(csv_file_name)