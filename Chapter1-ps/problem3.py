import os

# Function to list the contents of a directory
def list_directory_contents(directory_path):
    try:
        # Get the list of files and directories
        contents = os.listdir(directory_path)
        
        print(f"Contents of '{directory_path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory_path}'.")

# Provide the path of the directory you want to list
directory_path = input("/")

# Call the function
list_directory_contents(/)
