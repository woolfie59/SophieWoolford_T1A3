# T1A3 Terminal Application by Sophie Woolford

## R3 Referenced sources
https://peps.python.org/pep-0008/
https://github.com/Textualize/rich
https://realpython.com/python-csv/
https://www.markdownguide.org/extended-syntax/


## R4 GitHub repository
https://github.com/woolfie59/SophieWoolford_T1A3


## R5 Code style
- Following PEP8 style guide.
- Rich library.
- All defs, functions, and variables etc. are written using snake_case.
- Comments added for each section of code using "# 'comment'".


## R6 Application features
This application is a farming simulation game for a terminal. It consists of three main freatures; "Plant Crop", "Harvest Crop", and "View Crops". Upon starting the program, the user is shown a welcome message and a menu of choices. This is the main menu of the program. The menu options presented are the three features; plant, harvest, view, as well as an option to exit the program.

### "Plant Crop" Feature
The first feature, "Plant Crop", allows the user to plant one of three crops (broccoli, carrot, and potato). The selections is done from a menu which lists the three vegetables available to plant. The application then provides feedback to the user depending on what choice is made. The flow works as follows:
Menu: The `get_crop_choice()` function displays a menu of vegetables for the user to choose from to plant.
User input: The user is prompted to enter their selection. Error handling is in place to allow either uppercase or lowercase input which matches the options.
Processing input: The `plant_crop()` functions takes the user input, converts it to lowercase if uppercase was used, and then executes the corresponding action based on the chosen option.
Feedback: The program provides the user with feedback, a confirmation of whcihc vegetable has been planted. If an invalid input was made, an error message is displayed.
Looping: The program runs the loop the user ends it by selecting 'Exit' in the menu. Chosing to exit takes the user back to the main menu.

### "Harvest Crop" Feature
The second feature for this application is the "Harvest Crop" feature. This allow the user to choose one of three vegetables to harvest from a menu and then displays the input back to the user. To keep count of what crops have been harvested and their amounts for the 'View Crops' option in the main menu, a CSV file is created when the user selects a vegetable to harvest. This feature uses the following flow:
Creating CSV file: The functions 'read_vegetable_counts_from_csv()' and 'write_vegetable_counts_to_csv()' is the file handling used to keep track of the amounts and kinds of harvested vegetables. When the user chooses to harvest a vegetable, a CSV file is created to keep count.
Harvesting a vegetable: The 'harvest_crop()' function prompts the user to choose a vegetable to harvest through the 'get_harvest_choice()' function. When the user inputs a selection, the program adds one count to the CSV file.
Processing input: A message is displayed to the user then a harvest chocie has been made, confirming which vegetable has been harvested. This includes the display of an emoji of said vegetable to highlight the now existing vegetable. The user input is converted to lowercase if entered in uppercase, allowing either uppercase or lowercase input.
Looping: The program runs the loop the user ends it by selecting 'Exit' in the menu. Chosing to exit takes the user back to the main menu.

### "View Crops" Feature
The third and last feature is the "View Crops" feature. This allows the user to see the current count of each typ of vegetable they have harvested in the "Harvest Crop" feature. This feature flows as follows:
CSV file handling: The 'read_vegetable_counts_from_csv()' function reads the counts of vegetables from the CSV file 'vegetable_counts.csv'. This file is created when the user first harvests a vegetable in the "Harvest Crop" menu. If the user has not yet harvested a vegetable, an error message is displayed, prompting the user to plant and harvest a vegetable.
Display crops: The 'display_csv_content()' function reads the CSV file and displays the content to the user. The type of vegetable is show, along with the amount. If any vegetable has not been harvested yet, the counts is displayed as 0. At please one of either vegetable needs to have been harvested to view the CSV file. The 'view_crops()' function prints a header to indicate the "vegetable" and "count" columns, and calls the 'display_csv_content()' to show the count.


## R7 Implementation plan
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item
Utilise a suitable project management platform to track this implementation plan.
your checklists for each feature should have at least 5 items.
Answer: 


## R8 Help documentation
- To install the application
    - 

- Dependencies
    - Rich

- System requirements
    - MacOS/Linux/Windows
    - Python 3.9 or newer version

- how to use any command line arguments made for the application
