'''
Even so, in a file called lines.py, implement a program 
that expects exactly one command-line argument, the name 
(or path) of a Python file, and outputs the number of lines 
of code in that file, excluding comments and blank lines. 
If the user does not specify exactly one command-line argument, 
or if the specified file’s name does not end in .py, or if 
the specified file does not exist, the program should instead exit via sys.exit.

'''

import sys
import os.path

if len(sys.argv)==2:
    file_name, file_extension = os.path.splitext(sys.argv[1])
    exist = os.path.exists(sys.argv[1])

    if file_extension == ".py" and exist:
    
        with open(sys.argv[1]) as file:
            lines=file.readlines()
            not_blank_lines=0
            comment_lines=0
            for line in lines:
                if  line.strip(): # not_blank_lines = len([l for l in lines if l.strip()])
                    not_blank_lines += 1
                
                if line.startswith("#"):   # comment_lines= len([line for line in lines if line.startswith("#")])
                    comment_lines += 1

            complexity = not_blank_lines - comment_lines
            print(f"Number of lines: {complexity}")
        
    elif file_extension != ".py":
        sys.exit("Not a python file")
    elif exist == False:
        sys.exit("File doesn't exist.")

elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments.")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments.")



'''
if len(sys.argv)==2 and sys.argv[1].endswith('.py') and os.path.exists(sys.argv[1]):
    print("Found file")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments.")
elif os.path.splitext(sys.argv[1])[1] != ".py"
    sys.exit("Not a python file")
else:
    sys.exit("File doesn't exist.")
'''