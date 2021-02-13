#Program that asks for a string, reverses it, and print every second letter
#Author: Caio Forte Ribeiro

inputString = input("Please, type something here: ")

#now we slice the original string last index position
#moving until first index position with a step -2,
outputString = inputString[::-2]

print("Here's the weird string I got from yours:\n{}".format(outputString))