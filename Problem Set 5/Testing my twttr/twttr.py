'''
In a file called twttr.py, reimplement Setting up 
my twttr from Problem Set 2, restructuring your 
code per the below, wherein shorten expects a str
as input and returns that same str but with all 
vowels (A, E, I, O, and U) omitted, whether inputted 
in uppercase or lowercase.

Then, in a file called test_twttr.py, implement one or 
more functions that collectively test your implementation
of shorten thoroughly, each of whose names should begin 
with test_ so that you can execute your tests with: pytest test_twttr.py

'''
def main():
    text=input("Input: ")
    # print(f"Output: ", end="") 
    # shorten(text)
    print(f"Output: {shorten(text)}")
    


def shorten(word):
    a=""
    for txt in word:
        if txt.upper()=="A" or txt.upper()=="I" or txt.upper()=="E" or txt.upper()=="U" or txt.upper()=="O":
            # print("", sep="", end="")
            a +=""
        else:
            a +=txt
            # print(txt.casefold(), end="")
    return a


if __name__ == "__main__":
    main()


