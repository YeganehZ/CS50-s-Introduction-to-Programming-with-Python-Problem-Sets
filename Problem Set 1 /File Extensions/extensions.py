'''
In a file called extensions.py, implement a program that 
prompts the user for the name of a file and then outputs 
that file’s media type if the file’s name ends, case-insensitively, 
in any of these suffixes:

    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip

If the file’s name ends with some other suffix or has no suffix 
at all, output application/octet-stream instead, which is a 
common default.

'''

filename=input("What's the file name? ").lower()
if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpg"):
    print("image/jpg")
elif filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".txt"):
    print("text/txt")
elif filename.endswith(".zip"):
    print("folder/zip")
else:
    print("application/octet-stream")


'''
# Shorter code 
filename=input("What's the file name? ").lower()
ext= filename.split(".")
if ext[1] == "gif":
    print("image/gif")
elif ext[1] == "jpg":
    print("image/jpg")
elif ext[1] == "jpeg":
    print("image/jpeg")
elif ext[1] == "png":
    print("image/png")
elif ext[1] == "txt":
    print("text/txt")
elif ext[1] == "zip":
    print("folder/zip")
else:
    print("application/octet-stream")

'''