
from datetime import date
# from num2words import num2words
import inflect
import sys


def main():
    try:
        BDay= input("Date of Birth: ").split("-")
        birth_date=date(int(BDay[0]),int(BDay[1]),int(BDay[2]))
        todays_date = date.today()
        total_min= numOfMins(birth_date, todays_date)
        p = inflect.engine()
        print((p.number_to_words(total_min)).replace(" and", ""), "minutes")
    except (TypeError, ValueError):
        sys.exit("Invalid date")


def numOfMins(date1, date2):
  
    if date2 > date1:  
        return ((date2-date1).days*24*60) 
    else:
        return ((date1-date2).days*24*60)
 
 
if __name__ == "__main__":
    main()







