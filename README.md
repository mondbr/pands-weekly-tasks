<img src="https://vlegalwaymayo.atu.ie/pluginfile.php/1/theme_catawesome/logo/1708672446/logo.svg" width=20% height=20%>

# Programming and Scripting

author: Monika Dabrowska

This repository is for solutions to the weekly tasks for Programming and Scripting module on Higher Diploma in Data Analytics course from [ATU](https://www.atu.ie/).

I don't have any prevoius programming experience nor knowledge of basing coding, so I am using multiple sources and references to help me to complete the assignments. 

Each file contains comments to the code I am writing. Below I will explain my approach to solving the assigned task and reference the sources I researched for solving the problems. 

## Table of contents:
* [Weekly tasks](#weekly-tasks)
    * [Weekly task 01 - *helloworld.py*](#weekly-task-01---helloworldpy)
    * [Weekly task 02 - *bank.py*](#weekly-task-02---bankpy)
    * [Weekly task 03 - *accoutns.py*](#weekly-task-03---accoutnspy)
    * [Weekly task 03 Extra - *accounts_extra.py*](#weekly-task-03-extra---accounts_extrapy)
    * [Weekly task 04 - *collatz.py*](#weekly-task-04---collatzpy)
    * [Weekly task 05 - *weekday.py*](#weekly-task-05---weekdaypy)
    * [Weekly task 06 - *squareroot.py*](#weekly-task-06---squarerootpy)
    * [Weekly task 07 - *es.py*](#weekly-task-07---espy)
    * [Weekly task 08 - *plottask.py*](#weekly-task-08---plottaskpy)





# Weekly tasks


#### [Weekly task 01 - *helloworld.py*](https://github.com/mondbr/pands-weekly-tasks/blob/main/helloworld.py)

    Commit and push a file to the weekly tasks repository.
    This file should contain a python program that displays Hello World! when it is run.

A simple and traditional "Hello World!" program is often used as the first example when learning a new programming language or environment. It's designed to demonstrate the basic syntax and structure of a programming language by printing the text "Hello World!" to the output.

The output is: 

    Hello World!


#### [Weekly task 02 - *bank.py*](https://github.com/mondbr/pands-weekly-tasks/blob/main/bank.py)

    Write a program that should:

    Prompt the user and read in two money amounts (in cent)
    Add the two amounts
    Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount

I started with code to ask the user and read in two money amounts (in cent), then program add two amounts and convert it to two decimal numbers. 
The idea of how to take the sum of cents and convert it to represent money using decimal numbers was taken from [Stackoverflow.com](https://stackoverflow.com/questions/8637628/how-to-use-python-string-formatting-to-convert-an-integer-representing-cents-to).

The program is called: 

    $ python bank.py


User input:

    Enter your username: mondbr
    Enter amount1(in cent): 65
    Enter amount2(in cent): 180

The output is:

    The sum of these is €2.45



#### [Weekly task 03 - *accoutns.py*](https://github.com/mondbr/pands-weekly-tasks/blob/main/accounts.py)

    Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

This week we were looking at variables in python. The program I needed to write was very interesting for me as working with bank account numbers is related to my education and working experience. I started with code to ask the user to enter exaclty 10 digit number (bank account number). If the number of digits was incorrect, program is prompting an error message and asking to re-enter the number. Once correct number is entered, program is replacing first 6 digit with 'X', similiar to what we can see using bank or card numbers, where specific numbers are encrypted for secutiry reasons. 
The idea of how to replace digits was taken from [w3schools.com](https://www.w3schools.com/python/trypython.asp?filename=demo_string_replace).


The program is called: 
        
    $ accounts.py

User input:

    Please enter an 10 digit account number: 1234567890

The output is:

    XXXXXX7890
    
The error message if the number of digits is incorrect:

User input:

    Please enter an 10 digit account number: 1234

The output is:

    Invalid account number. Please enter exaclty 10 digits








#### [Weekly task 03 Extra - *accounts_extra.py*](https://github.com/mondbr/pands-weekly-tasks/blob/main/accounts_extra.py)

#### [Weekly task 04 - *collatz.py*](https://github.com/mondbr/pands-weekly-tasks/blob/main/collatz.py)

#### [Weekly task 05 - *weekday.py*](https://github.com/mondbr/pands-weekly-tasks/blob/main/weekday.py)

#### [Weekly task 06 - *squareroot.py*](https://github.com/mondbr/pands-weekly-tasks/blob/main/squareroot.py)


#### [Weekly task 07 - *es.py*](https://github.com/mondbr/pands-weekly-tasks/blob/main/es.py)

#### [Weekly task 08 - *plottask.py*](https://github.com/mondbr/pands-weekly-tasks/blob/main/plottask.py)









