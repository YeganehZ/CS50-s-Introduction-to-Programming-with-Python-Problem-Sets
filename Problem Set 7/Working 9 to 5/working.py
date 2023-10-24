'''
In a file called working.py, implement a function called convert 
that expects a str in either of the 12-hour formats below and 
returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). 
Expect that AM and PM will be capitalized (with no periods therein) 
and that there will be a space before each. Assume that these times 
are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

    9:00 AM to 5:00 PM
    9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in 
either of those formats or if either time is invalid 
(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that 
someone’s hours will start ante meridiem and end post meridiem; 
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to 
modify main and/or implement other functions as you see fit, 
but you may not import any other libraries. You’re welcome, 
but not required, to use re and/or sys.

Either before or after you implement convert in working.py, 
additionally implement, in a file called test_working.py, 
three or more functions that collectively test your implementation 
of convert thoroughly, each of whose names should begin with test_ 
o that you can execute your tests.

'''

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try: 
        if Hours :=re.search(r"^(\d{1,2})(\:(\d{2}))? (AM|PM) to (\d{1,2})(\:(\d{2}))? (PM|AM)$", s):
            
            flag1=0<=int(Hours.group(1))<=12 and 0<=int(Hours.group(5))<=12 and Hours.group(3)==None and Hours.group(7)==None
            flag2=0<=int(Hours.group(1))<=12 and 0<= int(Hours.group(5))<= 12 and 0<=int(0 if Hours.group(3) is None else Hours.group(3))<=59 and 0<= int(0 if Hours.group(7) is None else Hours.group(7))<= 59
            s1=s.split(" ")

            if flag1 or flag2:

                if Hours.group(4)== "AM" and Hours.group(8)== "AM":
                    return f"{int(Hours.group(1)) :02d}:{'00' if Hours.group(3)is None else Hours.group(3)} to {int(Hours.group(5)) :02d}:{'00' if Hours.group(7)is None else Hours.group(7)}"
                elif  Hours.group(4)== "AM" and Hours.group(8)== "PM":
                    return f"{int(Hours.group(1)) :02d}:{'00' if Hours.group(3)is None else Hours.group(3)} to {int(Hours.group(5)) + 12}:{'00' if Hours.group(7)is None else Hours.group(7)}"    
                elif Hours.group(4)== "PM" and Hours.group(8)== "AM":
                    return f"{int(Hours.group(1)) + 12}:{'00' if Hours.group(3)is None else Hours.group(3)} to {int(Hours.group(5)) :02d}:{'00' if Hours.group(7)is None else Hours.group(7)}"
                else:
                    return f"{int(Hours.group(1)) + 12}:{'00' if Hours.group(3)is None else Hours.group(3)} to {int(Hours.group(5)) + 12}:{'00' if Hours.group(7)is None else Hours.group(7)}"
                      
            else:
                raise ValueError
            

        else:
            raise ValueError
    except ValueError:
        sys.exit("Incorrect format")

    

if __name__ == "__main__":
    main()
