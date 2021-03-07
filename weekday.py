#Program that syas whether the current date is a weekday or not.
#Author: Caio Forte Ribeiro

import datetime

date = datetime.datetime.today().weekday()

if date < 5:
    print("Yes, unfortunately today is a weekday...")

else:
    print("Yay, it's weekend!")

