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

# New functions added below

def append_file_string(file_name, string_of_lines):
    try:
        # Appends the string to the end of the file
        with open(file_name, 'a') as file:
            file.write(string_of_lines)
    except Exception as e:
        print(f"Error appending to the file: {e}")

def write_file_list(file_name, list_of_lines):
    try:
        # Writes all items from the list to the file where each item is one line
        with open(file_name, 'w') as file:
            for line in list_of_lines:
                file.write(line + '\n')
    except Exception as e:
        print(f"Error writing to the file: {e}")

def copy_file_add_line_numbers(file_name_read, file_name_write):
    try:
        # Reads data from the first file, writes data to the new file, adding line numbers
        with open(file_name_read, 'r') as file_read:
            with open(file_name_write, 'w') as file_write:
                line_number = 1
                for line in file_read:
                    file_write.write(f"{line_number}:{line}")
                    line_number += 1
    except Exception as e:
        print(f"Error copying file with line numbers: {e}")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    # Ensure files are created or exist before operation
    create_data_file(file1)
    
    append_file_string(file1, string1)
    print(read_file_string(file1))
    
    write_file_list(file2, list1)
    print(read_file_string(file2))
    
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
