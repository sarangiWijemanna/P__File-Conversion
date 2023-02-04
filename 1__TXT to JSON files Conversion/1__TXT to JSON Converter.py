"1_ TXT to JSON files Converter"""

import json
import os


def checkHex(s):  # Function to check if the string represents a hexadecimal number
    # print(s)

    check = False

    if s[1:2] == "x":  # if location[1] in the string is "x"
        # print(s[2:])
        chrt = "abcdef"  # Can be character ---> a,b,c,d,e
        num = "0123456789"  # Numbers Can be from 0-9

        for selected_Ch in s[2:]:  # After Location[2] in Hexadecimal
            if (selected_Ch in chrt) or (selected_Ch in num):  # if selected_Character is abcdef or 0123456789
                check = True  # Satisfied the Check was True
            else:
                check = False  # Otherwise, Continue as False
    else:
        check = False

    return check  # True or False


# ......................................................................................................................
File_path = "file1.txt"  # Define the path of the Txt file
File_Name = os.path.basename(File_path)  # Get the name of the specified path
Name_Save_File = File_Name.split(".")[0]  # File Name separated by comma, Return the 1st item of the array
print(Name_Save_File)
File = open(File_path, "r")

Line_Number_Count = 1  # Declare the variable to save line number
lines = File.readlines()  # Read each lines in the list and stroke in list variable
print(lines)

# ......................................................................................................................
for line in lines:

    if line == "\n":  # Separate line by \n
        break
    print(line)

    Dictionary = {}  # Create Default Dictionary
    # key = ""  # Create Empty Key String

    line = line.split(" ")  # Split the line by space then store to the list variable
    print(line)
    print(len(line))

    # ...................................................................................................................
    element = 0  # Initialized the element i value is 0

    while element < len(line) - 1:
        if line[element + 1].isdigit():  # Check whether next element i+1 of the list is digit
            key = line[element]  # The key is current element i
            Dictionary[key] = line[element + 1]  # "Key" : "Digit i Value 0-9" ----> {'': '0'} {'': '0'} {'': '8'}
            element += 2  # Iterate the next element after the selected value
            # key = ""
            continue

        elif checkHex(line[element]):  # Call the checkHex function to check the string is Hexadecimal
            key = line[element]
            Dictionary[key] = line[element]  # "Key" : "Digit i Value 0-9" ----> {'': '0x90c000'} {'': '0x7fff'}
            element += 2  # Iterate the next element after the selected value
            # key = ""  # "Key" : "i Hexadecimal Value" ----> {'': '0x3fff'}
            continue

        else:  # Above conditions are not satisfied
            key = line[element] + " " + line[element + 1]  # Key = Current element+ Next element
            Dictionary[key] = line[element + 2]
            element += 3

    # print(Dictionary)  # Print dictionary in the terminal

    # ...................................................................................................................
    # Create JSON object as string
    json_object = json.dumps(Dictionary, indent=4)

    with open(
            "Converted json File.... " + Name_Save_File + "......Line of txt is..." + str(Line_Number_Count) + ".json",
            'w') as outfile:
        outfile.write(json_object)

    Line_Number_Count += 1
    # print(Line_Number_Count)
