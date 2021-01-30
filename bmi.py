#Asks for users' height and weight and calculates their Body Mass Index (BMI)
#Author: Caio Forte Ribeiro

#Reads height in cm and stores it as an integer in a variable "height"
height = int(input("Please, enter your height (in cm): "))

#Reads weight in kg and stores it as an integer in a variable "weight"
weight = int(input("Now enter your weight in kilograms: "))

#Calculates BMI as a function of weight divided by height (in metres) square
bmi = weight/((height/100)**2)

#Prints results
print("Your BMI is "+ str(bmi))