## FileOrganizer.py
# This script organizes files in a specified directory by type or size.
# It creates and populates subfolders for different file types and sizes.

##Import necessary libraries

import os
import shutil

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

## Main function to run the script

def main():
    ## Prompt user for the folder to organize
    # Ensure the user provides a valid folder name.
    valid = False
    while valid is False:
        folderChoice = input("Enter the folder to organize (e.g., 'Downloads', 'Documents'): ").strip()
        if folderChoice:
            directory = os.path.join(os.path.expanduser("~"), folderChoice)
            valid = True
        else:
            print("Invalid folder name. Please try again.")
    
    ## Prompt user for organization choice
    # Ask the user how they would like to organize their files.
    print("How would you like to organize your files?\n1. By Type\n2. By Size")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        organizeFilesByType(directory)
    elif choice == "2":
        organizeFilesBySize(directory)
    else:
        print("Invalid choice. Please enter 1 or 2.")

    print(f"Organizing files in: {directory}")

main()