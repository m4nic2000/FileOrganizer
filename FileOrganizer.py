## FileOrganizer.py
# This script organizes files in a specified directory by type or size.
# It creates and populates subfolders for different file types and sizes.

##Import necessary libraries

import os
import shutil
import guizero
from guizero import Window

## Define file type extensions and their corresponding folder names
# This dictionary maps file extensions to folder names for organization.

extensions = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".xlsx": "Spreadsheets",
    ".xls": "Spreadsheets",
    ".pptx": "Presentations",
    ".ppt": "Presentations",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".exe": "Executables",
}

## Define size categories and their corresponding folder names
# This dictionary maps size categories to folder names for organization.

size_folders = {
        "Small": 0,
        "Medium": 1024 * 1024,  # 1 MB
        "Large": 10 * 1024 * 1024,  # 10 MB
        "Huge": 100 * 1024 * 1024,  # 100 MB
    }

## Initialize an empty list for naming conventions
# This list will be used to store custom naming conventions for file organization.
folder_names = []

## Function to organize files by type
# This function iterates through files in the specified directory and moves them to subfolders based on their file type.

def organizeFilesByType(directory):
    ##Create folders for each file type if they do not exist
    for folder_name in set(extensions.values()):
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    ## Iterate through files in the directory
    # and move them to the appropriate subfolder based on their extension.    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            if extension in extensions:
                folder_name = extensions[extension]

                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)

                print(f"Moved: {filename} to {folder_name}")
            else:
                print(f"Skipping: {filename} (unknown file type)")
        else:
            print(f"Skipped: {filename} (it is a directory)")

    print("File organization complete.")

## Function to organize files by size
# This function categorizes files into folders based on their size.

def organizeFilesBySize(directory):
    ## Create folders for different size categories if they do not exist
    for folder_name in size_folders.keys():
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    ## Iterate through files in the directory
    # and move them to the appropriate subfolder based on their size.
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)

            if file_size < size_folders["Medium"]:
                folder_name = "Small"

                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)

                print(f"Moved: {filename} to {folder_name}")
            elif file_size < size_folders["Large"]:
                folder_name = "Medium"

                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)

                print(f"Moved: {filename} to {folder_name}")
            elif file_size < size_folders["Huge"]:
                folder_name = "Large"
                
                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)

                print(f"Moved: {filename} to {folder_name}")
            else:
                folder_name = "Huge"

                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)

                print(f"Moved: {filename} to {folder_name}")
        else:
            print(f"Skipped: {filename} (it is a directory)")

    print("File organization by size complete.")

##Function to organize files by naming conventions
# This function organizes files based on their naming conventions, such as prefixes or patterns.

def organizeFilesByNaming(directory):
    ## Create folders for custom naming conventions if they do not exist
    valid = False
    while not valid:
        naming_convention = input("Enter a prefix for like files(up to 5 characters):\nType finish to move on. ").strip()
        if naming_convention and len(naming_convention) <= 5:
            folder_path = os.path.join(directory, naming_convention)
            os.makedirs(folder_path, exist_ok=True)
            folder_names.append(folder_path)
            print(f"Created folder: {folder_path}")
        elif naming_convention.lower() == "finish":
            print("Exiting naming convention organization.")
            valid = True
        else:
            print("Invalid naming convention. Please try again.")
    
    ## Iterate through files in the directory
    # and move them to the appropriate subfolder based on their naming convention.
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            for folder_path in folder_names:
                if filename.startswith(os.path.basename(folder_path)):
                    destination_path = os.path.join(folder_path, filename)
                    shutil.move(file_path, destination_path)
                    print(f"Moved: {filename} to {folder_path}")
                    break
            else:
                print(f"Skipped: {filename} (no matching naming convention)")

    print("File organization by naming convention complete.")



## Main function to run the script

# def main():
#     ## Prompt user for the folder to organize
#     # Ensure the user provides a valid folder name.
#     valid = False
#     while valid is False:
#         folderChoice = input("Enter the folder to organize (e.g., 'Downloads', 'Documents'): ").strip()
#         if folderChoice:
#             directory = os.path.join(os.path.expanduser("~"), folderChoice)
#             valid = True
#         else:
#             print("Invalid folder name. Please try again.")
    
#     ## Prompt user for organization choice
#     # Ask the user how they would like to organize their files.
#     print("How would you like to organize your files?\n1. By Type\n2. By Size\n3. By Naming Convention")
#     choice = input("Enter 1, 2, or 3: ").strip()

#     if choice == "1":
#         organizeFilesByType(directory)
#     elif choice == "2":
#         organizeFilesBySize(directory)
#     elif choice == "3":
#         organizeFilesByNaming(directory)
#     else:
#         print("Invalid choice. Please enter 1 or 2.")

#     print(f"Organizing files in: {directory}")

## GUI for file organization

# User selection for folder organization
def open_folder():
    folder = guizero.select_folder(title="Select Folder to Organize")
    if folder:
        folder_path_text.value = (f"Selected folder: {folder}")
    else:
        print("No folder selected.")

# Function to assign folder names based on user input
def folder_name_assignment(name_list):
    name_list = name_list.split(",")
    folder_names.clear()  # Clear previous folder names
    for name in name_list:
        folder_names.append(name.strip())


# Create the GUI application
app = guizero.App(title="File Organizer", width=800, height=600)
# Add a welcome message and button to select the folder
message = guizero.Text(app, text="Welcome to File Organizer!\nPlease select the folder you want to organize.", size=14)
folder_select_button = guizero.PushButton(app, text="Organize Files", command=open_folder)
folder_path_text = guizero.Text(app, text="No folder selected")
# Add buttons for type and size organization
organize_by_type_button = guizero.PushButton(app, text="Organize by Type", command=lambda: organizeFilesByType(folder_path_text.value.split(": ")[1]))
organize_by_size_button = guizero.PushButton(app, text="Organize by Size", command=lambda: organizeFilesBySize(folder_path_text.value.split(": ")[1]))
# Add text input for custom naming conventions
custom_name_textbox = guizero.TextBox(app, text="Enter custom naming conventions (up to 5 characters), separated by commas:")
name_list = custom_name_textbox.value.split(",")
names_confirm_button = guizero.PushButton(app, text="Confirm Naming Conventions", command=lambda: folder_name_assignment(custom_name_textbox.value))
# Add button to organize by naming conventions
organize_by_naming_button = guizero.PushButton(app, text="Organize by Naming Convention", command=lambda: organizeFilesByNaming(folder_path_text.value.split(": ")[1]))
app.display()