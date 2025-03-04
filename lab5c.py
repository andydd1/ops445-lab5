#!/usr/bin/env python3
# Author ID: skkong4

def add(number1, number2):
    try:
        # Try to convert strings to numbers if they are not already
        number1 = float(number1) if isinstance(number1, str) else number1
        number2 = float(number2) if isinstance(number2, str) else number2
        
        # Perform the addition and return the result
        return number1 + number2
    except (ValueError, TypeError):
        # If there is an error (like invalid types that can't be converted), return an error message
        return 'error: could not add numbers'

def read_file(filename):
    try:
        # Try to read the file and return a list of all lines
        with open(filename, 'r') as file:
            return file.readlines()
    except Exception:
        # If there is an error (like the file not existing), return an error message
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # works, should print 15
    print(add('10', 5))                      # works, should print 15
    print(add('abc', 5))                     # exception, should print error message
    print(add('5', '5'))                     # works, should print 10
    print(read_file('seneca2.txt'))         # works, should print lines in the file
    print(read_file('file10000.txt'))       # exception, should print error message
