'''
In a file called scourgify.py, implement a program that:

    Expects the user to provide two command-line arguments:
        1. the name of an existing CSV file to read as input, 
        whose columns are assumed to be, in order, name and house, and
        2. the name of a new CSV to write as output, whose columns 
        should be, in order, first, last, and house.
    Converts that input to that output, splitting each name into a first
    name and last name. Assume that each student will have both a first 
    name and last name.

If the user does not provide exactly two command-line arguments, 
or if the first cannot be read, the program should exit via sys.exit
with an error message.

'''
import sys
import os.path
from tabulate import tabulate 
import csv

if len(sys.argv)==3:
    file_name, file_extension = os.path.splitext(sys.argv[1])
    exist = os.path.exists(sys.argv[1])

    if file_extension == ".csv" and exist:
    
        students=[]
        with open(sys.argv[1]) as file:
            reader=csv.DictReader(file)
            for row in reader: 
                students.append({"name": row["name"], "house": row["house"]})  
                
            students_new=[]
            for line in students:
                Name=line["name"]
                House=line["house"]
                first=Name.split(",")[1]
                last=Name.split(",")[0]
                students_new.append({"first": first, "last": last, "house": House})
            #print(students_new)
            
            with open(sys.argv[2], "a", newline="") as file:
                writer=csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writerow({"first":"first", "last":"last", "house":"house"})
                for student in students_new:
                    writer.writerow(student)

    else:
        sys.exit(f"Could not read {sys.argv[1]}.")

elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments.")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments.")