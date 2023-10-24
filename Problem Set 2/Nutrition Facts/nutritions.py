'''
In a file called nutrition.py, implement a program that prompts 
consumers users to input a fruit (case-insensitively) and then 
outputs the number of calories in one portion of that fruit, per 
the FDA’s poster for fruits, which is also available as text. 
Capitalization aside, assume that users will input fruits exactly 
as written in the poster (e.g., strawberries, not strawberry). 
Ignore any input that isn’t a fruit.

'''

Items=input("Item: ").lower()

match Items:
    case "apple":
        print("Calories: 130")
    case "avocado":
        print("Calories: 50")
    case "banana":
        print("Calories: 110")
    case "cantaloupe":
        print("Calories: 50")
    case "grapefruit":
        print("Calories: 60")
    case "grapes":
        print("Calories: 90")
    case "honeydew Melon":
        print("Calories: 50")
    case "kiwifruit":
        print("Calories: 90")
    case "lemon":
        print("Calories: 15")
    case "lime":
        print("Calories: 20")
    case "nectarine":
        print("Calories: 60")
    case "orange":
        print("Calories: 80")
    case "peach":
        print("Calories: 60")
    case "pear":
        print("Calories: 100")
    case "pineapple":
        print("Calories: 50")
    case "plums":
        print("Calories: 70")
    case "strawberries":
        print("Calories: 50")
    case "sweet Cherries":
        print("Calories: 100")
    case "tangerine":
        print("Calories: 50")
    case "watermelon":
        print("Calories: 80")