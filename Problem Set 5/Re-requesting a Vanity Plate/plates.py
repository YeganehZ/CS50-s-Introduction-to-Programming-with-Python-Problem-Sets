'''
In Massachusetts, home to Harvard University, it’s possible 
to request a vanity license plate for your car, with your 
choice of letters and numbers instead of random ones. 
Among the requirements, though, are:

    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) 
    and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they 
    must come at the end. For example, AAA222 would be an acceptable … 
    vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for 
a vanity plate and then output Valid if meets all of the 
requirements or Invalid if it does not. Assume that any 
letters in the user’s input will be uppercase. Structure 
your program per the below, wherein is_valid returns True if s 
meets all requirements and False if it does not. Assume that s 
will be a str. You’re welcome to implement additional functions 
for is_valid to call (e.g., one function per requirement).

'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag1=1
    flag2=1
    flag3=1
    flag4=1
    flag5=1
    j=0
    
    if s[0].isalpha() and s[1].isalpha() and 2 <= len(s) <= 6:
        for argument in range(len(s)):
            if s[argument].isdigit() or s[argument].isalpha():
                if s[argument].isdigit() and s[argument]=="0" and j==0:
                    j=j+1
                    flag1=0
                elif s[argument].isdigit() and s[argument]!="0" and j==0:
                    j=j+1
                elif j>0 and argument==len(s)-1 and s[argument].isalpha():
                    flag2=0
                else:
                    flag3=1
            else:
                flag4=0
    else: 
        flag5=0
   
    if flag1 and flag2 and flag3 and flag4 and flag5:
        return True
    else:
        return False



if __name__=="__main__":
    main()
