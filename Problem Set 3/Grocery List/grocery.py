'''
In a file called grocery.py, implement a program 
that prompts the user for items, one per line, 
until the user inputs control-d (which is a common 
way of ending one’s input to a program). 
Then output the user’s grocery list in all uppercase, 
sorted alphabetically by item, prefixing each line 
with the number of times the user inputted that item. 
No need to pluralize the items. Treat the user’s input case-insensitively.

'''

from collections import Counter
my_list = [ ]
 
while True:
     try:
         my_list.append(input())
     
     except EOFError:
        break
                 
item_counts = Counter(my_list)
print(item_counts)
for item, count in sorted(item_counts.items()):
    print(f"{count} {item.upper()}")

    



