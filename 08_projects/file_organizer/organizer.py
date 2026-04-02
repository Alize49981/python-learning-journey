import os
import shutil

# Folder to organize (change this to your path)
folder_path = "."

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Python": [".py"],
    "Documents": [".txt", ".pdf"]
}

# Loop through files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(file)

    # Check file type
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            target_folder = os.path.join(folder_path, folder)

            # Create folder if not exists
            os.makedirs(target_folder, exist_ok=True)

            # Move file
            shutil.move(file_path, os.path.join(target_folder, file))

            print(f"Moved {file} to {folder}")
            break