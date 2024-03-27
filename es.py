# program that reads in a text file and outputs the number of e's it contains. 
# author: Monika Dabrowska



import os

while True:
    file_name = input("Enter the text file name in format: xxxx.txt ") #asking user to enter file name
    print("You entered:", file_name)

    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            # Read the content of the file
            content = f.read()
            # Count the occurrences of 'e' (case-insensitive)
            count = content.lower().count('e')
        print ("Number of letters 'e' (case-insensitive) in the file is", count)
        break
    else:
        print (file_name, "file does not exist, please enter another file name.")