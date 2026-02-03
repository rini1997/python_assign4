"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""
from logging import exception
lineCount = 0
try:
    file_container = open("sample.txt", "rt")
    while True:
        try:
            line = file_container.readline()
            if not line:  # EOF reached
                break
            lineCount=lineCount+1
            print(f"Line {lineCount}: {line}", end="")
        except:
            break
except FileNotFoundError as e:
    print(f"Error: {e.strerror}: '{e.filename}'")
except Exception as e:
    print(f"Error: {e}")








