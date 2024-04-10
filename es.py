# program that reads in a text file and outputs the number of e's it contains. 
# author: Monika Dabrowska



import sys
# importing sys so it can take a command line argument
# https://www.quora.com/How-can-I-pass-a-list-of-file-names-as-a-command-line-argument-to-a-Python-script


import os
# importing os so it can check for various conditions such as file does not exist, or a file that is not a text file
# https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/
# https://stackoverflow.com/questions/57007680/how-to-handle-the-exception-when-input-file-does-not-exists-in-python


file_name = sys.argv[1]
# sys.argv[1] beacuse sys.argv[0] is the first argument which is the name of py file we are starting

# Check if the file exists
# https://www.geeksforgeeks.org/python-os-path-exists-method/

if not os.path.exists(file_name): 
    print("File does not exist")
    sys.exit(1)
    # https://stackoverflow.com/questions/9426045/difference-between-exit0-and-exit1-in-python

# Check if the file is a text file
# https://www.programiz.com/python-programming/methods/string/endswith

if not file_name.lower().endswith('.txt'):  
    print("File is not a text file")
    sys.exit(1)
    # https://stackoverflow.com/questions/9426045/difference-between-exit0-and-exit1-in-python



with open(file_name, 'r') as f:
    es = f.read()
    # counting "e" character in the file
    count = es.count("e") + es.count("E")
    # if we write count = es.count("e") + es.count("E") it will give us a count of both upper and lowercase character
    print (count)





 









