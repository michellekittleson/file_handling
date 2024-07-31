'''
1. Exploring Python's OS Module

Task 1: Directory Inspector

Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.

'''

import os

def list_directory_contents(path, directory):
    if path in directory:
        print(os.listdir())

