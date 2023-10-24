'''
In a file called response.py, using either validator-collection or 
validators from PyPI, implement a program that prompts the user for 
an email address via input and then prints Valid or Invalid, respectively, 
if the input is a syntatically valid email address. You may not use re. 
And do not validate whether the email address’s domain name actually exists.

'''
import sys
from validator_collection import validators

try:
    if email_address := validators.email(input("What's your email address? ").strip()):
        print("Valid")
    else:
        print("Invalid")

except (ValueError, TypeError):
    sys.exit("Invalid")
