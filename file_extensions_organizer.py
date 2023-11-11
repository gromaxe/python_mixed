# File Organizer
import os

def organize_directory(path, verbose=0):
    """
    Organizes files in the specified directory into subfolders based on file type.

    Each file is moved to a subfolder named after its file extension. If the subfolder
    does not exist, it is created. Files without an extension are moved to a
    'No extension' folder.

    Parameters:
    path (str): The path of the directory whose files are to be organized.
    verbose (int): The verbosity level (0: no output, 1: folders created, 2: files moved).

    Example usage:
    organize_directory("/path/to/directory", verbose=1)
    """

    # Check if the path exists and is a directory
    if not os.path.exists(path) or not os.path.isdir(path):
        print(f"The provided path '{path}' is not a valid directory.")
        return -1

    created_folders = set()
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            parts = file.split('.')
            file_type = parts[-1] if len(parts) > 1 else "No extension"
            new_dir = os.path.join(path, file_type)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir, exist_ok=True)
                created_folders.add(new_dir)
                if verbose >= 1:
                    print(f"Created folder: {new_dir}")

            if verbose >= 2:
                print(f"Moving {file} to {new_dir}")
            os.rename(os.path.join(path, file), os.path.join(new_dir, file))

if __name__ == "__main__":
    directory_path = input("Enter the path of the directory to organize: ")
    if organize_directory(directory_path) != -1:  # Default verbosity level is 0 (silent)
        print("Files organized.")
