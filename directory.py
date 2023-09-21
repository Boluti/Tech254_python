import os

def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

# Tells the user to enter a directory name
directory_name = input("Enter a directory name: ")

# Call the create_directory function to create the directory
create_directory(directory_name)