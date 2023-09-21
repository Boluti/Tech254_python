import os

def echo_string(string):
    os.system(f"echo {string}")

# Prompt the user to enter a string
user = input("Enter a string: ")

# Call the echo_string function to echo the input string
echo_string(user)