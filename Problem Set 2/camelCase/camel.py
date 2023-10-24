'''
In a file called camel.py, implement a program that 
prompts the user for the name of a variable in camel 
case and outputs the corresponding name in snake case.
 Assume that the user’s input will indeed be in camel case.

'''
camel=input("camelCase: ")
print("snake_case: ", sep="", end="")
for c in camel:
    if c.isupper():
     print ("_",c.lower(), sep="", end="")
    else:
        print(c, end="")

   
   