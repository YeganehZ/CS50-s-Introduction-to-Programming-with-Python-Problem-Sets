'''
In a file called bank.py, implement a program that prompts
the user for a greeting. If the greeting starts with “hello”, 
output $0. If the greeting starts with an “h” (but not “hello”), 
output $20. Otherwise, output $100. Ignore any leading whitespace 
in the user’s greeting, and treat the user’s greeting case-insensitively.

'''

def main():
    INPUT=str(input("How are you greeted? "))
    print(f"${value(INPUT)}")

def value(greeting):
    greeting=greeting.lower().strip()
    if "hello" in greeting:
        return 0
    elif greeting[0] == "h" and "hello" not in greeting:
        return 20
    else:
        return 100
    

if __name__ == "__main__":
    main()


''' without defining functions:

greetings=input("How are you greeted? ").lower().strip()

if "hello" in greetings:
    print("$0")
elif greetings[0]== "h" and "hello" not in greetings:
    print("$20")
else:
    print("$100")

'''
