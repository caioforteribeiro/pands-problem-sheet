#Asks for users' height and weight and calculates their Body Mass Index (BMI)
#Author: Caio Forte Ribeiro

#Reads height in cm and stores it as a float in a variable "height"
height = float(input("Please, enter your height (in cm): "))

#Reads weight in kg and stores it as a float in a variable "weight"
weight = float(input("Now enter your weight in kilograms: "))

#Calculates BMI as a function of weight divided by height (in metres) square
bmi = weight/((height/100)**2)

#Round function to display only 2 decimals
#Converts BMI into str and prints results
print("Your BMI is "+ str(round(bmi,2))) 