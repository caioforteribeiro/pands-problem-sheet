#Program that uses a newly created funcion to calculate square roots
#Input should be a float and output should be an approximation
#Author: Caio Forte Ribeiro

#Define a funcion sqrt with 2 arguments
def sqrt (n, precision):
    x = n 

    while (float(n > 0)) :
        
        #Newton's method formula    
        root = 0.5 * (x + (n / x)) 

        #Keeps calculating until the difference 
        #between the actual root and the guess (x)
        #is minimal (as set in precision)         
        
        if abs(root - x) < precision:
            break 
        
        #Returns the last calculated number for x
        x = root
    
    return root

num = float(input("Enter a positive number: "))

#Asks for a positive float if user enters 0 or a negative
while num <= 0:
    num = float(input("Enter a positive number: "))

#precision of 0.001 is enough to calculate
#squareroots rounded to 1 decimal
rootNum = round(sqrt(num, 0.001), 1)

print("The squareroot of {} is approximately {}" .format(num,rootNum))