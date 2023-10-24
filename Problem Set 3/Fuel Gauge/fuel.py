'''
In a file called fuel.py, implement a program that 
prompts the user for a fraction, formatted as X/Y, 
wherein each of X and Y is an integer, and then 
outputs, as a percentage rounded to the nearest 
integer, how much fuel is in the tank. If, though, 
1% or less remains, output E instead to indicate 
that the tank is essentially empty. And if 99% or 
more remains, output F instead to indicate that the 
tank is essentially full.

If, though, X or Y is not an integer, X is greater 
than Y, or Y is 0, instead prompt the user again. 
(It is not necessary for Y to be 4.) Be sure to 
catch any exceptions like ValueError or ZeroDivisionError.

'''


def main():
    while True:
        try:
            frac= input("Fraction: ")
            percent=convert(frac)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            pass
    

def convert(fraction):
    fraction=fraction.split("/")
    if int(fraction[0]) > int(fraction[1]) and int(fraction[1]) !=0 :
        raise ValueError    
    elif int(fraction[1])==0:
        raise ZeroDivisionError

    percentage= round(int(fraction[0])/int(fraction[1])*100) 
    return percentage



def gauge(percentage):

    if 0<= percentage <= 1:
        return f"E"   
    elif 99 <= percentage <=100 :
        return f"F" 
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()








