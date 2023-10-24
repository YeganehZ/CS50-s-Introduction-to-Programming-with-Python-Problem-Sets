'''

In deep.py, implement a program that prompts the user 
for the answer to the Great Question of Life, the Universe 
and Everything, outputting Yes if the user inputs 42 or 
(case-insensitively) forty-two or forty two. Otherwise output No.

'''

Question=input("What's the answer to the great question of life, universe, and everything? ").lower()

if Question=="forty-two" or Question=="forty two" or Question=="42":
    print("Yes")
else:
    print("No")
