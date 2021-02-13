#Program that asks for a positive int
#outputs list starting at initial number,
#and calculates next values using the following logic:
#if number is even, divide it by 2; if odd, multiply by 3 and add 1
#list stops at 1.
#Author: Caio Forte Ribeiro


#creates an empty list
myList = []

#asks for user input and converts into int
number = int(input("Enter a number:\n"))

#Throws an error and asks for new input if user enters invalid numbers (< 1)
while number < 1:
    number = int(input("Enter a positive number, greater than or equal to 1:\n"))

#appends list with first number
myList.append(number)                    

while number > 1:
    #checks if number is even,
    #divides number by 2 and stores it in number
    if number % 2 == 0:                   
        number //= 2

    #if number is odd,
    #multiply by 3 and add 1
    else:                                 
        number = int(number * 3 + 1)  

    #adds resulting number to the list
    myList.append(number)

#prints final list, from initial number to 1
print(myList)