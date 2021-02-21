# Problem sheet (Weeekly Assignments)

## Week 02

### Task
Write a program (**bmi.py**) that takes values of height (in cm) and weight (in kg) and returns the user's Body Mass Index (BMI).

### Code
```python
height = float(input("Please, enter your height (in cm): "))
weight = float(input("Now enter your weight in kilograms: "))

bmi = weight/((height/100)**2)

print("Your BMI is "+ str(round(bmi,2)))

```

### Notes & Comments
Body Mass Index is a method for screening the relative weight of a person, and is measured by taking the person's weight in kilograms divided by the square of height in metres

For this program, we first needed to ask the 2 basic inputs from the user (**height** and **weight**) and store the values in their corresponding variables. We expected these variables to be floats, as both height and weight are continuous data.

To calculate the user's BMI, the value of weight was divided by the squared value of height, and the result was stored in the variable **bmi** (bmi = weight(kg) / [height (m)<sup>2</sup>]). We opted to convert **height** to metres (by dividing the input value by 100) directly in the BMI formula, rather than creating a new variable to store the converted value. The **round** funtion was used to limit the number of decimals in the resulting BMI to 2.

### References
- BMI definition: [US CDC Website](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html). Access on 21 Feb, 2021.
- Using the round function to limit decimals: David Amos. [How to Round Numbers in Python](https://realpython.com/python-rounding/), Real Python. Access on 21 Feb, 2021.


## Week 03

### Task
Write a program (**secondstring.py**) that reads a string and outputs every second character of the reversed string. 

### Code
```python
inputString = input("Please, type something here: ")
outputString = inputString[::-2]

print("Here's the weird string I got from yours:\n{}".format(outputString))

```

### Notes & Comments
There are many methods for reversing strings in Python. The quickest, and probably the easiest one is through slicing.
To reverse by using the slicing method, we use the following argument/syntax:
inputString = "Some text"
outputString = inputString[::-n], where [(first index):(last index):(step)]

### References
- Reversing a string through slicing: [How to Reverse a String in Python](https://www.w3schools.com/python/python_howto_reverse_string.asp), W3 Schools. Access on 21 Feb, 2021.
Other methods to reverse strings: [Python Reverse String – 5 Ways and the Best One](https://www.journaldev.com/23647/python-reverse-string), JournalDev. Access on 21 Feb, 2021.


