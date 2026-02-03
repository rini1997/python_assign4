"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""
"create file output.txt"
import pickle
with open("output.txt","x") as fb :
    input_text = input("Enter text to write to the file : ")
    fb.write(input_text)
    fb.close()
with open("output.txt", "a") as file:
    append_text = input("Enter text to append to the file: ")
    file.write("\n"+append_text)
    file.close()
with open("output.txt", "r") as file:
    print("The Final output of the file output.txt is:")
    for line in file:
        print(line.strip())