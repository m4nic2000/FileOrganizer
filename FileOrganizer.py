## FileOrganizer.py
# This script organizes files in a specified directory by type or size.
# It creates and populates subfolders for different file types and sizes.

##Import necessary libraries

import os
import shutil
from guizero import App, Text, PushButton, TextBox, select_folder, info

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
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        return

    # Create folders for each file type if they do not exist
    for folder_name in set(extensions.values()):
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):  # Check if folder exists
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created folder: {folder_name}")

    # Iterate through files in the directory and move them based on their extension
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            if extension in extensions:
                folder_name = extensions[extension]
                folder_path = os.path.join(directory, folder_name)
                destination_path = os.path.join(folder_path, filename)

                # Check if file exists before moving
                if os.path.exists(file_path):
                    shutil.move(file_path, destination_path)
                    print(f"Moved: {filename} to {folder_name}")
                else:
                    print(f"Error: File not found - {filename}")
            else:
                print(f"Skipping: {filename} (unknown file type)")
        else:
            print(f"Skipped: {filename} (it is a directory)")

    print("File organization complete.")

## Function to organize files by size
# This function categorizes files into folders based on their size.

def organizeFilesBySize(directory):
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        return

    # Create folders for each size category
    for folder_name in size_folders.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created folder: {folder_name}")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            try:
                file_size = os.path.getsize(file_path)
                
                if file_size < size_folders["Medium"]:
                    folder_name = "Small"
                elif file_size < size_folders["Large"]:
                    folder_name = "Medium"
                elif file_size < size_folders["Huge"]:
                    folder_name = "Large"
                else:
                    folder_name = "Huge"

                destination_folder = os.path.join(directory, folder_name)
                destination_path = os.path.join(destination_folder, filename)

                shutil.move(file_path, destination_path)
                print(f"Moved: {filename} to {folder_name}")
            except FileNotFoundError as e:
                print(f"File not found: {file_path}. Error: {e}")
            except Exception as e:
                print(f"Error moving file {filename}: {e}")
        else:
            print(f"Skipped: {filename} (it is a directory)")

    print("File organization by size complete.")

##Function to organize files by naming conventions
# This function organizes files based on their naming conventions, such as prefixes or patterns.

def organizeFilesByNaming(directory):
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        return

    if not folder_names:
        print("No naming conventions provided. Please enter custom naming conventions.")
        return

    # Create folders for custom naming conventions
    for name in folder_names:
        folder_path = os.path.join(directory, name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created folder: {name}")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            matched = False
            for prefix in folder_names:
                if filename.startswith(prefix):
                    destination_folder = os.path.join(directory, prefix)
                    destination_path = os.path.join(destination_folder, filename)
                    try:
                        shutil.move(file_path, destination_path)
                        print(f"Moved: {filename} to {prefix}")
                        matched = True
                        break
                    except FileNotFoundError as e:
                        print(f"File not found: {file_path}. Error: {e}")
                        break
                    except Exception as e:
                        print(f"Error moving file {filename}: {e}")
                        break
            if not matched:
                print(f"Skipped: {filename} (no matching naming convention)")
        else:
            print(f"Skipped: {filename} (it is a directory)")

    print("File organization by naming convention complete.")

## GUI for file organization

# User selection for folder organization
def open_folder():
    folder = select_folder(title="Select Folder to Organize")
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

# Function to get the selected folder from the GUI
def get_selected_folder():
    text = folder_path_text.value
    if text.startswith("Selected folder: "):
        folder = text.split(": ", 1)[1]
        if os.path.isdir(folder):
            return folder
        else:
            info("Error", f"Selected folder does not exist: {folder}")
            return None
    else:
        info("Error", "Please select a valid folder first.")
        return None
    
# Function ensuring a valid folder is selected
def run_if_folder_selected(callback):
    folder = get_selected_folder()
    if folder:
        callback(folder)


# Create the GUI application
app = App(title="File Organizer", width=800, height=600)
# Add a welcome message and button to select the folder
message = Text(app, text="Welcome to File Organizer!\nPlease select the folder you want to organize.", size=14)
folder_select_button = PushButton(app, text="Organize Files", command=open_folder)
folder_path_text = Text(app, text="No folder selected")
# Add buttons for type and size organization
organize_by_type_button = PushButton(app, text="Organize by Type", command=lambda: run_if_folder_selected(organizeFilesByType))
organize_by_size_button = PushButton(app, text="Organize by Size", command=lambda: run_if_folder_selected(organizeFilesBySize))
# Add text input for custom naming conventions
custom_name_textbox = TextBox(app, text="Enter custom naming conventions (up to 5 characters), separated by commas:")
names_confirm_button = PushButton(app, text="Confirm Naming Conventions", command=lambda: folder_name_assignment(custom_name_textbox.value))
# Add button to organize by naming conventions
organize_by_naming_button = PushButton(app, text="Organize by Naming Convention", command=lambda: run_if_folder_selected(organizeFilesByNaming))
app.display()