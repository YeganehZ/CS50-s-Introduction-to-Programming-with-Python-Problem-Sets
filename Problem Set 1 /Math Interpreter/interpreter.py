'''
In a file called interpreter.py, implement a program that 
prompts the user for an arithmetic expression and then 
calculates and outputs the result as a floating-point value 
formatted to one decimal place. Assume that the user’s input 
will be formatted as x y z, with one space between x and y and 
one space between y and z, wherein:

    x is an integer
    y is +, -, *, or /
    z is an integer

For instance, if the user inputs 1 + 1, your program should 
output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, 
so will your interpreter.py be an interpreter for math!

'''

math_expression=input("What's the arthematic expression? ").replace(" ", "")
x=int(math_expression[0])
y=math_expression[1]
z=int(math_expression[2])

if y == "+":
   print(float(x + z))
elif y== "-":
    print(float(x-z))
elif y== "*":
    print(float(x*z))
elif y== "/":
    if z == 0:
        print("Division not defined")
    else:
        print(float(x/z))
else:
    print("Arthemetic operator not defined")
