# System packages
import os.path, csv

# External packages
import rich
from rich import print
from rich.console import Console

console = Console()

# Imports of own functions
from farm_functions import plant_crop, harvest_crop, view_crops

# Welcome message
print("\n[bold]Welcome to your farm![/bold]", ":cowboy_hat_face:", ":seedling:")

# Main menu
def farm_menu():
    print("\nTo [bold]plant[/bold] a crop, enter [bold]1[/bold].")
    print("To [bold]harvest[/bold] a crop, enter [bold]2[/bold].")
    print("To [bold]view[/bold] your crops, enter [bold]3[/bold].")
    print("To [bold]leave[/bold] your farm, enter [bold]4[/bold].")

    user_choice = input("\nPlease enter your selection: ")
    return user_choice

choice = ""

# While loop for main menu selections
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
        print("\n   [bold red]You goofball! Select 1 or 2 or 3 or 4 from the menu.[/bold red]")

# Exit message
print("See ya later, farmer!", ":cowboy_hat_face:\n")
