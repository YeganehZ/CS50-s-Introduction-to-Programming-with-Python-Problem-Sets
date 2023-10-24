'''
In a file called pizza.py, implement a program that 
expects exactly one command-line argument, the name 
(or path) of a CSV file in Pinocchio’s format, and 
outputs a table formatted as ASCII art using tabulate, 
a package on PyPI at pypi.org/project/tabulate. 
Format the table using the library’s grid format. 
If the user does not specify exactly one command-line 
argument, or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.

'''
import sys
import os.path
from tabulate import tabulate 
import csv

if len(sys.argv)==2:
    file_name, file_extension = os.path.splitext(sys.argv[1])
    exist = os.path.exists(sys.argv[1])

    if file_extension == ".csv" and exist:
    
        pizzas=[]
        with open(sys.argv[1]) as file:
            reader=csv.reader(file)
            for row in reader: 
                pizzas.append(row)                
            
            print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))

        
    elif file_extension != ".csv":
        sys.exit("Not a csv file")
    elif exist == False:
        sys.exit("File doesn't exist.")

elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments.")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments.")