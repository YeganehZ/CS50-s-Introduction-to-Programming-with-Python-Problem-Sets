'''
After finishing CS50 itself, students on campus at 
Harvard traditionally receive their very own I took 
CS50 t-shirt. No need to buy one online, but like to try one on virtually?

In a file called shirt.py, implement a program that 
expects exactly two command-line arguments:

    in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent 
background) on the input after resizing and cropping the input to 
be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, 
resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, 
using default values for method, bleed, and centering, overlay the shirt with Image.paste, 
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, 
and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

    if the user does not specify exactly two command-line arguments,
    if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    if the input’s name does not have the same extension as the output’s name, or
    if the specified input does not exist.

Assume that the input will be a photo of someone posing in just 
the right way, like these demos, so that, when they’re resized 
and cropped, the shirt appears to fit perfectly.

'''
import sys
import os.path
from tabulate import tabulate 
from PIL import Image, ImageOps

if len(sys.argv)==3:
    file_name1, file_extension1 = os.path.splitext(sys.argv[1])
    file_name2, file_extension2 = os.path.splitext(sys.argv[2])
    exist = os.path.exists(sys.argv[1])

    file_formats=[".png", ".jpg", ".jpeg"]


    if (file_extension1 in file_formats) and (file_extension2 in file_formats) and file_extension1 == file_extension2 and exist:
        Input=Image.open(sys.argv[1])
        SHIRT=Image.open("shirt" + file_extension1)

        Input1=ImageOps.fit(Input, (600,600), method=0, bleed=0.0, centering=(0.5, 0.5))

        Input1.paste(SHIRT, (0,0), SHIRT)
        Input1.save(sys.argv[2])    



    elif file_extension1 != file_extension2:
        sys.exit("Input and output have different extensions.")
    elif exist == "False":
        sys.exit("Invalid input.")
    else:
        sys.exit("Wrong file names")

elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments.")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments.")