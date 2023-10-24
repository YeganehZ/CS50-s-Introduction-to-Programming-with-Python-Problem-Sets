'''
In a file called numb3rs.py, implement a function 
called validate that expects an IPv4 address as 
input as a str and then returns True or False, 
respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome 
to modify main and/or implement other functions as you 
see fit, but you may not import any other libraries. 
You’re welcome, but not required, to use re and/or sys.

Either before or after you implement validate in numb3rs.py, 
additionally implement, in a file called test_numb3rs.py, 
two or more functions that collectively test your implementation 
of validate thoroughly, each of whose names should begin with test_ .

'''
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):    
    if matches := re.match("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        code=re.split(r"\.", ip)
        flag=0 
        for i in range(len(code)):
            if 0 <= int(code[i]) < 256:
                flag += 0
            else:
                flag += 1
                
        if flag ==0:
            return True
        else:
            return False 
    
    else:
        sys.exit("False")



if __name__ == "__main__":
    main()
