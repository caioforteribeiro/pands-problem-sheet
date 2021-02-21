# Problem sheet (Weekly Assignments)

For reference on how to format README GitHub documents (*.md):
[Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax), GitHub Docs. Access on 19 Feb, 2021.



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

For this program, we first needed to ask the 2 basic inputs from the user (`height` and `weight`) and store the values in their corresponding variables. We expected these variables to be floats, as both height and weight are continuous data.

To calculate the user's BMI, the value of weight was divided by the squared value of height, and the result was stored in the variable `bmi` (bmi = weight(kg) / [height (m)<sup>2</sup>]). We opted to convert `height` to metres (by dividing the input value by 100) directly in the BMI formula, rather than creating a new variable to store the converted value. The `round` funtion was used to limit the number of decimals in the resulting BMI to 2.

### References
- **BMI definition:** [US CDC Website](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html). Access on 21 Feb, 2021.
- **Using the round function to limit decimals:** David Amos, [How to Round Numbers in Python](https://realpython.com/python-rounding/), Real Python. Access on 21 Feb, 2021.



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
```python
inputString = "Some text"
outputString = inputString[::-n]
```
Where [(first index):(last index):(step)]. `[::-2]` is therefore instructing the program to read the string from the last indexed character all the way to the first, with a step of -2 (i.e. reading one character, jumping the next, and so on).

### References
- **Reversing a string through slicing:** [How to Reverse a String in Python](https://www.w3schools.com/python/python_howto_reverse_string.asp), W3 Schools. Access on 21 Feb, 2021.
- **Other methods to reverse strings:** [Python Reverse String – 5 Ways and the Best One](https://www.journaldev.com/23647/python-reverse-string), JournalDev. Access on 21 Feb, 2021.



## Week 04

### Task
Write a program that prints out a Collatz sequence (**collatz.py**) starting from any integer that the user inputs.

### Code
```python
myList = []

number = int(input("Enter a number:\n"))

while number < 1:
    number = int(input("Enter a positive number, greater than or equal to 1:\n"))

myList.append(number)                    

while number > 1:

    if number % 2 == 0:                   
        number //= 2

    else:                                 
        number = int(number * 3 + 1)  

    myList.append(number)

print(myList)

```

### Notes & Comments
The Collatz sequence starts with a positive integer (*n*) and get new terms added to the sequence by using the following calculation:
- If the previous term is *even*, the next term is equal to the previous term divided by 2.
- If the previous term is *odd*, the next term is equal to the previous term multiplied by 3 plus 1 (***3n + 1***).

The code starts by declaring an empty list (`myList`) and asking for the user's input, as an integer to be stored in the variable `number`. If the user's input is 0 or a negative number, the program asks for a new input (the Collatz sequence requires that the start number is a positive integer greater than or equal to 1):

```python
while number < 1:
    number = int(input("Enter a positive number, greater than or equal to 1:\n"))

```
If the input is valid, the program adds it to the list and then starts to add new numbers using `if` and `else` statements until `number` reaches 1:
```python
if number % 2 == 0:                   
        number //= 2

    else:                                 
        number = int(number * 3 + 1)  

    myList.append(number)

```
As the final step, the program prints out the resulting list, from the user's input all the way to 1.

### References
- **About the Collatz sequence:*** [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture), Wikipedia. Access on 21 Feb, 2021.
  - **The Collatz Sequence:** Al Sweigart. [Automate the Boring Stuff with Python. Chapter 3 - Functions](https://automatetheboringstuff.com/chapter3/). Access on 21 Feb, 2021. The author declares a function, with the `while`, `if` and `else`statements, and stores the sequence in a string rather then in a list. The solution can be found [here](https://codereview.stackexchange.com/questions/229270/python-the-collatz-sequence).



## Week 05

### Task


### Code


### Notes & Comments


### References