#!/usr/bin/env python3
# Author ID: skkong4

import os

def create_data_file(file_name):
    # Check if the file exists, and create it with default content if it doesn't
    if not os.path.exists(file_name):
        try:
            with open(file_name, 'w') as file:
                file.write("Hello World\nThis is the second line\nThird line\nLast line\n")
        except Exception as e:
            print(f"Error creating the file: {e}")
            return False
    return True

def read_file_string(file_name):
    try:
        # Takes file_name as string for a file name, returns its entire contents as a string
        with open(file_name, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading the file as a string: {e}")
        return ""

def read_file_list(file_name):
    try:
        # Takes a file_name as string for a file name, 
        # return its entire contents as a list of lines without new-line characters
        with open(file_name, 'r') as file:
            return [line.rstrip('\n') for line in file]
    except Exception as e:
        print(f"Error reading the file as a list: {e}")
        return []

if __name__ == '__main__':
    file_name = 'data.txt'
    # Ensure the file exists before reading it
    if not create_data_file(file_name):
        print("Failed to create the file. Exiting...")
        exit(1)

    # Try to read and print the file contents
    file_content_string = read_file_string(file_name)
    if file_content_string:
        print(file_content_string)

    file_content_list = read_file_list(file_name)
    if file_content_list:
        print(file_content_list)
