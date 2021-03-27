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
Write a program (**weekday.py**) that checks the current date is a weekday or not.

### Code
```python
import datetime

date = datetime.datetime.today().weekday()

if date < 5:
    print("Yes, unfortunately today is a weekday...")

else:
    print("Yay, it's weekend!")

```

### Notes & Comments
First we needed to import the `datetime` module, which allows us to operate more easily with dates and times. The method `datetime.today()` extracts the current date, and the `date.weekday()` method returns an integer that maps the day of the week, starting on 0 (Monday) all the way  to 6 (Sunday). To check if the current date is a weekday, we simply concatenate the 2 methods, store it in a variable `date`, and see if it's less than 5 (which means, from 0 to 4, or from Monday to Friday). If so, the program prints that it's a weekday. If not (i.e. if it's 5 or 6), the program prints that it's weekend. 

### References
- **Weekday() Method Of Datetime Class In Python:** [Pythonic](https://pythontic.com/datetime/datetime/weekday). Access on 14 March, 2021.
- **datetime — Basic date and time types:** [The Python Standard Library](https://docs.python.org/3/library/datetime.html). Access on 14 March, 2021.
- **How do I get the day of week given a date?:** [Stack Overflow](https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date). Access on 14 March, 2021.



## Week 06

### Task
Write a program (**squareroot.py**) that returns an approximation of the square root of a positive float number, without using built-in functions.

### Code
```python
def sqrt (n, precision):
    x = n 

    while (float(n > 0)) :    
        root = 0.5 * (x + (n / x))          
        
        if abs(root - x) < precision:
            break 
        
        x = root
    
    return root

num = float(input("Enter a positive number: "))

while num <= 0:
    num = float(input("Enter a positive number: "))

rootNum = round(sqrt(num, 0.001), 1)

print("The squareroot of {} is approximately {}" .format(num,rootNum))

```

### Notes & Comments
We start the program by defining a function `sqrt`, which takes two arguments: `n` (the number to be rooted), and `precision` (the degree of precision for an approximation of the result using the Newton's method - the smallest the number for this argument, the higher the precision and the better the approximation). The function calculates 'guesses' (`x`) that are ever closer to the actual root until it reaches the desired precision, measured as the difference between the actual root and the different guesses. The formula for the calculation is known as the Newton's method, which is a method for guessing approximations of the actual root of a given number. If we don't define the precision (or a limit to how accurate we want the result to be), the program runs indefinitely.

After defining the function,  we apply it to num (which is a float number input by the user). Negative inputs are rejected using a `while` loop until the user enters a positive number. As our results will be round to only 1 decimal, setting a precision of 0.001 is enough (setting a lower precision might lead to wrong results for numbers between 0 and 1, like 0.1 or 0.5 - our assumption was that the numbers should be positive, not necessarily higher than 1). Finally, the program prints out the result. 

### References
- [Newton's Method](https://en.wikipedia.org/wiki/Newton%27s_method), Wikipedia. Access on 27 March, 2021.
- ["Simplified" Newton method of finding roots](https://math.stackexchange.com/questions/2278545/simplified-newton-method-of-finding-roots), Stack Exchange. Access on 27 March, 2021.
- Jerry L. Kazdan, [Finding Square Roots Using Newton’s Method](https://www2.math.upenn.edu/~kazdan/202F09/sqrt.pdf), University of Pennsylvania. Access on 27 March, 2021.
- [Python Functions](https://www.w3schools.com/python/python_functions.asp), W3 Schools. Access on 27 March, 2021.
- **Newton´s Method using Python:**
  - [Newton's Method](https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/), Mathematical Python. Access on 27 March, 2021.
  - [Find root of a number using Newton’s method](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method), Geeks for Geeks. Access on 27 March, 2021.


## Week 07

### Task
Write a program (**es.py**) that reads a text file (.txt) and prints out how many times the character 'e' appears in it.

### Code
```python
import sys

filename = sys.argv[1]

with open(filename, "rt") as f:
    content = f.read()

print(content.count("e"))

```

### Notes & Coments
The program starts by importing the `sys` module, so we're able to fetch arguments from the command line. Then, we store the 2nd argument of the command line into a variable `filename`, using `sys.argv`. The program opens the file in read mode and the resulting string is stored into `content` (we can test it using the `type()` function). To print out the number of e's, then, we can simply use the string method `count()`.

### References
- **Getting an argument from the command line:**
  - Nandan Kumar, [How to use sys.argv in Python](https://www.knowledgehut.com/blog/programming/sys-argv-python-examples), Knowledge Hut. Access on 14 March, 2021.
  - [sys — System-specific parameters and functions](https://docs.python.org/3/library/sys.html), The Python Standard Library. Access on 14 March, 2021.
- **Handling files in Python:**  
  - Vuyisile Ndlovu, [Working With Files in Python](https://realpython.com/working-with-files-in-python/), Real Python. Access on 14 March, 2021.
  - [Python File Handling](https://www.w3schools.com/python/python_file_handling.asp), W3 Schools. Access on 14 March, 2021.
- **f.read() returning a string in *text* mode:** [The Python Tutorial - Input and Output](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects), Python.org. Access on 14 March, 2021.
- **The count() method:**: [Python - String Methods](https://www.w3schools.com/python/python_strings_methods.asp), W3 Schools. Access on 14 March, 2021.


## Week 08

### Task
Write a program (**plottask.py**) that plots the following functions in the range [0, 4]:
f(x) = x
g(x) = x^2
h(x) = x^3
The plots must use the same set of axis.

### Code
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
f = x
g = x**2
h = x**3

fontTitle = {"family": "calibri", 
             "color" : "#342e2e", 
             "size": "18"
             }

fontAxis = {"family": "calibri",
            "color" : "#342e2e", 
            "size": "12"
            }

plt.rcParams["axes.facecolor"] = "#f5f5f5"
plt.rcParams["lines.linewidth"] = 3
plt.rcParams["figure.facecolor"] = "#f5f5f5"

plt.title("Plots", fontdict = fontTitle)
plt.xlabel("x", fontdict = fontAxis) 
plt.ylabel("Functions", fontdict = fontAxis)

plt.plot(x, f, color = "#58508d", label = "$f(x) = x$")
plt.plot(x, g, color = "#ff6361", label = "$g(x) = x^{2}$")
plt.plot(x, h, color = "#ffa600", label = "$h(x) = x^{3}$")

plt.legend()
plt.grid()
plt.show()
```

### Notes & Comments
We start the program by importing the `numpy` module, so we can operate with our variable `x` as an array within a fixed range (from 0 to 4), and `matplotlib.pyplot`, to plot our functions.
`x` is defined used the `array` funtion of `np`. We can then call the values for the y-axis as dependent of `x`.
The remainder of the code is all about customising and displaying the plotting, by changing colours, line width, defining labels, adding a legend, a title and a grid. For this program, we chose to configure our customisations directly in the script by using `plt.rcParam`, instead of having a separate style sheet for that.


### References
- [NumPy Creating Arrays](https://www.w3schools.com/python/numpy_creating_arrays.asp), W3 Schools. Access on 20 March, 2021.
- Matplotlib rcParams: [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/tutorials/introductory/customizing.html), Matplotlib.org. Access on 20 March, 2021.
- Customising text and labels: [Controlling style of text and labels using a dictionary](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html), M.org. Access on 20 March, 2021.
- [Changing fonts in matplotlib](https://stackoverflow.com/questions/45877746/changing-fonts-in-matplotlib), Stack Overflow. Access on 20 March, 2021.
- [Matplotlib Adding Grid Lines](https://www.w3schools.com/python/matplotlib_grid.asp), W3 Schools. Access on 20 March, 2021.
- Colour palette source for lines: [Data Color Picker](https://learnui.design/tools/data-color-picker.html#palette), Learn UI Design. Access on 20 March, 2021.
- HEX codes for background and font colours:
  - [White Smoke](https://www.eggradients.com/color/white-smoke-color), Eggradients. Access on 20 March, 2021.
  - [Mine Shaft](https://www.eggradients.com/shades-of-black-color), Eggradients. Access on 20 March, 2021.